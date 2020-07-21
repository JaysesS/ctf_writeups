# sage solve.sage

from sage.all import *
from Crypto.Util.number import *

def coppersmith_short_pad(c1, c2, n):
    """When provided with two ciphertexts of the same message but with different (short)
    paddings, i.e.
        C1 = (M | r1)^3 = M1^3 and
        C2 = (M | r2)^3 = M2^3),
    this function calculates the difference r2 - r1 of the two (random) paddings used
    during encryption using Coppersmith's method. Afterwards, the Franklin-Reiter
    attack can be applied to recover the plaintext.
    See http://www.di.ens.fr/~fouque/ens-rennes/coppersmith.pdf
    Returns all possible values for the difference in a list.
    """
    # Fixed exponent.
    e = 3

    # Create two polynomial rings and corresponding variables. Sage cannot calculate the resultant
    # in a ring of integers modulo N, so we'll use and integer ring for that, then switch rings afterwards.
    RZmodN.<xm> = PolynomialRing(Zmod(n))
    RZ.<x, y> = PolynomialRing(ZZ)

    # Create the two polynomials g1 and g2. If y = r2 - r1, then g1 and g2 both have the root M1.
    g1 = x**e - c1
    g2 = (x + y)**e - c2

    # Calculate the resultant. The resultant is the product of the differences of the roots of the
    # two polynomials. As seen above, for the case that y = r2 - r1, both polynomials have the same
    # root M1, thus r2 - r1 is a root of the resultant of g1 and g2.
    p = g1.resultant(g2)

    #
    # Now let sage do all the work by calculating small roots of the resultant.
    #

    # We need a univariate polynomial for this. At this point, x should be eliminated though.
    p = p.univariate_polynomial()
    # Change rings. We need the ring of integers modulo N now.
    p = p.change_ring(RZmodN).subs(y = xm)
    # Make sure the polynomial is monic, i.e. the coefficient of x^(p.degree()) is 1.
    p = p.monic()
    # Now let sage to the magic. Try to find all small roots of p using Coppersmith's method.
    return p.small_roots(X=2**(512 // 9), beta=0.5)

def franklin_reiter(c1, c2, n, a=1, b=1):
    """Recovers the plain text message from the two cipher texts knowing
    that they were both encrypted using the exponent 3 and that
    M2 = a * M1 + b.
    See https://www.cs.unc.edu/~reiter/papers/1996/Eurocrypt.pdf
    Returns both plain text messages as a tuple.
    """
    f = b*(c2 + 2*(a**3)*c1 - b**3  ) % n
    g = a*(c2 - a**3*c1     + 2*b**3) % n

    # Calculage f / g: f / g = f * g**(-1) = f * inverse_mod(g, n)
    gi = inverse_mod(g, n)
    m = f * gi % n

    return (m, m+b)


N = 163741039289512913448211316444208415089696281156598707546239939060930005300801050041110593445808590019811244791595198691653105173667082682192119631702680644123546329907362913533410257711393278981293987091294252121612050351292239086354120710656815218407878832422193841935690159084860401941224426397820742950923L

E = 3

C1 = 110524539798470366613834133888472781069399552085868942087632499354651575111511036068021885688092481936060366815322764760005015342876190750877958695168393505027738910101191528175868547818851667359542590042073677436170569507102025782872063324950368166532649021589734367946954269468844281238141036170008727208883L

C2 = 42406837735093367941682857892181550522346220427504754988544140886997339709785380303682471368168102002682892652577294324286913907635616629790484019421641636805493203989143298536257296680179745122126655008200829607192191208919525797616523271426092158734972067387818678258432674493723618035248340048171787246777L


roots = coppersmith_short_pad(C1, C2, N)
d = roots[0]
if d >= 2**32:
    C1, C2 = C2, C1
    d = -d

m, _ = franklin_reiter(C1, C2, N, b=int(d))

# brute long bits
k = 0
while True:
    msg = long_to_bytes(m << k)
    if "flag{" in msg:
        print(msg)
        break
    k+=1
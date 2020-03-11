int __cdecl main(int argc, const char **argv, const char **envp)
{
  size_t v3; // rax
  char s; // [rsp+0h] [rbp-110h]
  unsigned int v6; // [rsp+100h] [rbp-10h]

  v6 = -559038737;
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  printf("Magic value: 0x%08x\nFill the buffer: ", 3735928559LL);
  gets(&s);
  v3 = strlen(&s);
  printf("Got %u bytes.\n", v3);
  printf("Magic value: 0x%08x\n", v6);
  if ( v6 == -790693170 )
  {
    printf("Ya, cool, here is your flag: ");
    system("cat /flag");
  }
  else
  {
    printf("Try harder");
  }
  return 0;
}
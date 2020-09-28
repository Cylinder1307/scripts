#include <stdio.h>
#include <stdlib.h>

int main(void) {
  // setting up the script

  int option, score;
  int score_add = 1;
  int score_take = 2;
  system("clear");

  // printing credits and choices

  printf("Chelp.c\n");
  printf("Developed and maintained by Cylinder1307");
  printf("\n");
  printf("\n");
  printf("1) Help\n2) Please help\n3) Please help this is terrible\n4) Don't help\n\n");

  // getting user input

  printf("Your choice:    ");
  scanf("%d", &option);
  printf("\n");

  // if else with user input

  if ( option == 1 ) {
    printf("Thank you, this was getting frustrating\n");
    score = score+10;
  }
  else if ( option == 2 ) {
    printf("Took you long enough\n");
    score = score + score_add;
  }
  else if ( option == 3 ) {
    printf("Finally\n");
    score = score - score_take;
  }
  else {
    printf("Fuck you bitch\n");
    score = score - 1000;
  }

  // finding and printing the score assigned in the last step
  printf("Your score is %d", score);

}

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

#define kTryTimes 30
#define kTryBase 2

int main(void){
  
  srand((unsigned)time(NULL));

  float random_x, random_y;
  int num_in_circle = 0;
  int cycle_pick_num;
  float pi; 

  for(int cycle_try=0; cycle_try<kTryTimes; ++cycle_try){
    cycle_pick_num = pow(kTryBase, cycle_try);
    num_in_circle = 0;
   
    for(int cycle_pick=0; cycle_pick<cycle_pick_num; ++cycle_pick){
      random_x = rand()/(float)(RAND_MAX);
      random_y = rand()/(float)(RAND_MAX);

      if((random_x*random_x+random_y*random_y)<1.00000){
        ++num_in_circle;
      }
    }

    pi = 4 * (num_in_circle * 1.0 / cycle_pick_num);
    printf("%d===>%f\n", cycle_try, pi);
  }

  return 0;
}

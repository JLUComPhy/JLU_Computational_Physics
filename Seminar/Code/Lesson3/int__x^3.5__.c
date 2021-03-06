#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<stdbool.h>
#include<math.h>

bool is_underside(float, float);

int main(void){
  
  float random_x, random_y;
  int kTryNumber =30;
  int kTryGapBase = 2;
  int point_num = 1;
  int underside_times = 0;
  float int_res;

  srand((unsigned)time(NULL));  //A seed for random number
  
  for(int try_cycle=0; try_cycle<kTryNumber; ++try_cycle){
    point_num *= kTryGapBase;
    underside_times = 0;
    for(int throw_cycle=0; throw_cycle<point_num; ++throw_cycle){
      random_x = rand()/((float)(RAND_MAX));
      random_y = rand()/((float)(RAND_MAX));
      
      if(is_underside(random_x, random_y)){
        ++underside_times;
      } 
    }
    int_res = ((float)(underside_times))/point_num;
    printf("2^%d  %d  %f\n", try_cycle+1, point_num, int_res);
  }

  return 0;
}

bool is_underside(float x, float y){
 
  float function_y;
   
  function_y = pow(x, 3.5);

  if(function_y>y){
    return true;
  }
  else{
    return false;
  }
}

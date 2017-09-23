#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define kLeftPossible 0.5
#define kStreetWidth 10
#define kInitPosition 1
#define kTryTimes 100000
#define kTotalWalkStep 10000

int main(void){

  srand((unsigned)time(NULL));

  int position;
  float next_possible;
  int record_data[kStreetWidth];

  for(int cycle_init_record_data=0; cycle_init_record_data<kStreetWidth; ++cycle_init_record_data){
    record_data[cycle_init_record_data] = 0;
  }

  for(int cycle_try=0; cycle_try<kTryTimes; ++cycle_try){
    position = kInitPosition;

    for(int cycle_walk=0; cycle_walk<kTotalWalkStep; ++cycle_walk){
      
      next_possible = rand()/(float)(RAND_MAX);

      if(((next_possible<kLeftPossible)) && (position!=0)){
        --position;
      }
      if(((next_possible>kLeftPossible)) && (position!=kStreetWidth-1)){
        ++position;
      }
    }

    ++record_data[position];
  }

  for(int cycle_print_res=0; cycle_print_res<kStreetWidth; ++cycle_print_res){
    printf("%d      %f\n", cycle_print_res, record_data[cycle_print_res]*1.0/kTryTimes);
  }

  return 0;
}
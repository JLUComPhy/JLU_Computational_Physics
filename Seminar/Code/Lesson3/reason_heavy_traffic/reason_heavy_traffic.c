#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define kVehicleNum  100
#define kTimeRevelution  200
#define kLimitDistance 10
#define kLimitVelocity 30
#define kInitVelocity 5
#define kInitDistance 20
#define kPossibleDecelerate 0.4

int main(void){

  int all_velocity[kVehicleNum];
  int all_distance[kVehicleNum];
  int plot_vehicle[kVehicleNum];
  int count_distance = 0;
  
  srand((unsigned)time(NULL));

  for(int cycle_init=0; cycle_init<kVehicleNum; ++cycle_init){
    all_velocity[cycle_init] = kInitVelocity;
    all_distance[cycle_init] = kInitDistance;
  }
 
  for(int cycle_revelution=0; cycle_revelution<kTimeRevelution; ++cycle_revelution){
    
    for(int cycle_drive=0; cycle_drive<kVehicleNum; ++cycle_drive){
      if(all_distance[cycle_drive]>=kLimitDistance){
        if(rand()/(float)(RAND_MAX)<kPossibleDecelerate){
          --all_velocity[cycle_drive];
        }
        else{
          ++all_velocity[cycle_drive];
        }        
      }
      else{
        --all_velocity[cycle_drive];
      }

      if(all_velocity[cycle_drive]<0){
        all_velocity[cycle_drive] = 0;
      }
      if(all_velocity[cycle_drive]>kLimitVelocity){
        all_velocity[cycle_drive] = kLimitVelocity;
      }
    }

    for(int cycle_distance=0; cycle_distance<kVehicleNum-1; ++cycle_distance){

      all_distance[cycle_distance] -= all_velocity[cycle_distance] - all_velocity[cycle_distance+1];

      if(all_distance[cycle_distance]<0){
        all_distance[cycle_distance] = 0;
      }
    }

    //count_distance = 0;
    for(int cycle_plot_data=0; cycle_plot_data<kVehicleNum; ++cycle_plot_data){
      
      plot_vehicle[cycle_plot_data] = count_distance;

      printf("%d  %d\n", cycle_revelution, plot_vehicle[cycle_plot_data]);

      count_distance += all_distance[cycle_plot_data];
    }
    count_distance = all_distance[0];
  }

  return 0;
}
#include <stdio.h>

int josephus_survivor(int n, int k){

    int circle[n];
    int i;

    for(i=0; i<n;i++){
        circle[i] = i+1;
        // printf("%d", circle[i]);
    }

    int counter = 0;
    int t = 0;
    int j;
    int num_out = 0;

    while(num_out < n-1){
        // printf("hello");
        for(j=0; j<n; j++){
            if (circle[j] != 0){
                counter++;
            }
            if(num_out == n-1){
                break;
            }
            if (counter == k){
                circle[j] = 0;
                counter = 0;
                num_out++;
                // printf("%d", num_out);
            }
        }
    }

    int out = 0;
    for(i=0; i<n;i++){
        // printf("\n%d", circle[i]);
        if (circle[i] != 0){
            out = circle[i];
        }
    }


    return out;
}

int main(){
    int a = josephus_survivor(2545,1302);
    printf("%d", a);
    return 0;
}

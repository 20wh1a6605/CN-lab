#include<stdio.h>
#include<string.h>
int main(){
    int d;
    char str[100];
    printf("Give the data to be decrypted\n");
    scanf("%[^\n]%*c",str);
    printf("Give the key value\n");
    scanf("%d",&d);
    for(int i = 0;i<strlen(str);i++){
        if(str[i] != ' '){
            str[i] = str[i] - d;
            }
        }
    printf("%s",str);
    }

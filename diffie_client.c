// Client side C/C++ program to demonstrate Socket programming
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#define PORT 8080

int ModPow(int x, int y, int p)
{
    int res = 1;
    x = x % p;
    while (y > 0)
    {
    if ((y & 1) == 1){
        res = (res*x) % p;
        // std::cout << res <<" = " <<(res*x) <<  " mod(" << p << ")\n";
    }
    y = y>>1;
    x = (x*x) % p;
    }
    return res;
}

int main(int argc, char const *argv[])
{
    struct sockaddr_in address;
    long long int P = 353, pr = 3, Xa, Xb, Ya, Yb, K1, K2;
    int sock = 0, valread;
    struct sockaddr_in serv_addr;
    char *hello = "Hello from client";
    char buffer[1024] = {0};

    printf("Enter value for Xb: ");
    scanf("%lld", &Xb);

    Yb = ModPow(pr, Xb, P);
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }
  
    memset(&serv_addr, '0', sizeof(serv_addr));
  
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
      
    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) 
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
  
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }
    send(sock , (const char*)&Yb , strlen((const char*)&Yb) , 0 );
    printf("Hello message sent\n");
    valread = read( sock , buffer, 1024);
    printf("%s\n",buffer );
    return 0;
}
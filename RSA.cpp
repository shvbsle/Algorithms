/*
SHIV's RSA Algorithm
*/

#include<iostream>
#include<math.h>
#include<cstdlib>

int check_prime(unsigned long int n);
unsigned long int encrypt(unsigned long int, unsigned long int, unsigned long int);
unsigned long int decrypt(unsigned long int, unsigned long int, unsigned long int);
unsigned long int jpl(unsigned long int, unsigned long int, unsigned long int);



int main()
{

  double r;
  int a;
  unsigned long int p, q, n, phin, e, d, k;
  unsigned long int c, m, mm;


// generate 2 prime numbers < 100
  
  a = 0;

  // while(a==0) { 
  // r = ((double) rand() / (RAND_MAX));
  // p = int(r*100.0);
  // a = check_prime(p); 
  // }

  // a = 0;

  // while(a==0) { 
  // r = ((double) rand() / (RAND_MAX));
  // q = int(r*100.0);
  // a = check_prime(q); 
  // }
  std::cout << "Enter p: " ;
  std::cin >> p;
  std::cout << "Enter q: " ;
  std::cin >> q;

  std::cout<<"p,q = "<<p<<" "<<q<<"\n";

  n = p*q;
  phin = (p-1)*(q-1);


// generate e such that 1<e<phin, e and phin are coprime

 
  a = 0;

  while(a==0) { 
  r = ((double) rand() / (RAND_MAX));
  e = int(0.1*r*double(phin));
  a = check_prime(e); 
  }

  std::cout<<"public key, n, e: "<<n<<" "<<e<<" \n";


// generate private key, d

  k = 5;
  while((1+k*phin)%e!=0){
   k++;
  }

  d = (1 + k*phin)/e; 

  std::cout<<" k, d "<<k<<" "<<d<<" \n";


//  secret message to be encrypted
   std::cout<<"\n enter secret message to be encrypted: \n";
   std::cin>>m;


//  encrypt message

  c = encrypt(n,e,m); 

  std::cout<<"encrypted message: "<<c<<" \n";   


// decrypt message

  mm = decrypt(n,d,c);

  std::cout<<"decrypted message "<<mm<<" \n";



  return 0;
}



// check for prime: return 1 if prime; 0 otherwise
int check_prime(unsigned long int n)
{

  unsigned long int i;

  for(i = 2; i<= sqrt(n); i++)
  {
   if(n%i == 0){
     return 0;
   }
  }

  return 1;
}


// encrypt
unsigned long int encrypt(unsigned long int n, unsigned long int e, unsigned long int m)
{
  unsigned long int c, i;
  
  c = jpl(m,e,n); 
  return c;
}


// decrypt
unsigned long int decrypt(unsigned long int n, unsigned long int d, unsigned long int c)
{
  unsigned long int m;
  
  m = jpl(c,d,n);
  return m;
}


// (b^e)%m
unsigned long int jpl(unsigned long int b, unsigned long int e, unsigned long int m)
{

 unsigned long int c, e1; 
  
 c = 1;
 e1 = 0;

 while(e1<e){
  e1++;
  c = (b*c)%m;
 } 

 return c; 
}



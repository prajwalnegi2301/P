'''for(int i=0;i<n;i++){
        for(int j=n-i;j>=0;j--){
            cout<<" ";

        }
        for(int j=0;j<i+1;j++){
            cout<<"*";


        }
        for(int l=0;l<i;l++){
            cout<<"*";
        }

        cout<<endl;


    }'''
n= 3
for i in range(n):
    print(" " * (n - i  ), "*" * (i+1))
'''n=3
for i in range (3):
    print("*" * (i+1))'''


'''n=3
for i in range(3):
    print(" "* (n-i-1) , "*" * (i+1))'''
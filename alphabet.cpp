#include<iostream>
using namespace std;
int main(){
    char character;
    int position;
    cin>>character;

    if (character>='a' && character<='z'){
        cout<<"lowercase"<<endl;
        position = character - 'a' + 1;
        cout<<position;
    }
    else if (character>='A' && character<='Z'){
        cout<<"uppercase"<<endl;
        position = character - 'A' + 1;
        cout<<position;
    }
    else{
        cout<<"error";
    }
    return 0;
}

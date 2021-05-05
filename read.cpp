#include<iostream>

#include<cctype>//isalpha()

#include <cstring>//strlen()

#include <cmath>//round()

#include<string>

using namespace std;

int main() {

    string text;

    cout << "Enter your text: ";
    getline(cin, text);


    //initializing our Variables
    int n;
    n = text.size();

    int letters = 0, words = 1, sentences = 0;

    for (int i = 0; i <= n; i++) {

        char charecter = text[i];

        if (isalpha(charecter))
            letters++;

        if (charecter == ' ')
            words++;

        if (charecter == '.' || charecter == '?' || charecter == '!')
            sentences++;

    }

    float L = (float(letters) * 100) / float(words);
    float S = (float(sentences) * 100) / float(words);

    float sum = (0.0588 * L) - (0.296 * S) - 15.8;

    float index = round(sum);

    if (index < 1) {
        cout << "befor Grade 1";
    }
    else if (index > 16) {
        cout << "Grade +16";
    }
    else
        cout << "Grade " << index;

    system("pause>0");
    return 0;
}
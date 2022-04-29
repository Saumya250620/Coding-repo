#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    cout << s << endl;
    s = "Hello world,123!";
    // s.insert(1, "see");
    // s.replace(1,3,"X12");
    cout << s.find("l") << endl;
    cout << s.substr(3,5) << endl;
    // s.append("132");
    cout << s << endl;

    // s = "Some text!";
    // cout << s << endl;
    // cout << s.at(1) << endl;

    // string word;
    // cout << "Enter the word: ";
    // cin >> word;
    // s = s + word;
    // cout << s << endl;
    // cout << s.length() << endl;
    system("pause");
    return 0;
}
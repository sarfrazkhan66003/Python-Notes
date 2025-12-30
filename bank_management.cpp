/*Write a program in C++ to bank mangement system using OOP's 
with file handling for beginners.*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Bank
{
public:
      string name, address, phone, email, accountno, accounttype;
       double balance; 
      void deposit(double amount)
    {
        balance += amount;
    }

    void withdraw(double amount)
    {
        if (amount <= balance, amount > 0)
            balance -= amount;
            
        else
            cout << "Insufficient balance!" << endl;
    }

    double balance_inquiry()
    {
        return balance;
    }

    void transfer(double amount) // Transfer money from one account to another
    {
        if (amount <= balance)
        {
            balance -= amount;
        }
        else
            cout << "Insufficient balance!" << endl;
    
    }   
};
void create_account()   
{ 
    Bank b;
    ofstream outfile;
    outfile.open("Bank.txt", ios::app);      // open the file with write permission and append  
    cout << "Enter Your Name: "<<endl;
    cin >> b.name;
    cout << "Enter Your Address: "<<endl;
    cin >> b.address;
    cout << "Enter Your Phone Number: "<<endl;
    cin >> b.phone;
    cout << "Enter Your Email: "<<endl;
    cin >> b.email;
    cout << "Enter Your Account Number: "<<endl;
    cin >> b.accountno;
    cout << "Enter Your Account Type: "<<endl;
    cin >> b.accounttype;
    cout << "Enter Your Balance: "<<endl;
    cin >> b.balance;
    outfile << b.name << " " << b.address << " " << b.phone << " " << b.email<< " " << b.accountno << " " << b.accounttype << " " << b.balance << "\n";
    outfile.close();
    cout << "\nYour Account Has Been Created Successfully\n\n";
}
int display_account()
{
    Bank b;
    ifstream infile;    
    infile.open("Bank.txt");
    while (infile >> b.name >> b.address >> b.phone >> b.email >> b.accountno >> b.accounttype >> b.balance)      
    {
        cout << "Name: " << b.name << endl;
        cout << "Address: " << b.address << endl;
        cout << "Phone: " << b.phone << endl;
        cout << "Email: " << b.email << endl;
        cout << "Account Number: " << b.accountno << endl;
        cout << "Account Type: " << b.accounttype << endl;
        cout << "Balance: " << b.balance << endl;
    }
    infile.close();
    return 0;
}
void modify_account(string n, string v)
{     
    Bank b;
    fstream file; 
    file.open("Bank.txt", ios::in);
    ofstream temp;
    temp.open("Temp.txt");
    while (file >> b.name >> b.address >> b.phone >> b.email >> b.accountno >> b.accounttype >> b.balance)
    {
        if (b.name == n)
        {
            cout << "Enter New Name: "<<endl;
            cin >> b.name;
            cout << "Enter New Address: "<<endl;
            cin >> b.address;
            cout << "Enter New Phone: "<<endl;
            cin >> b.phone;
            cout << "Enter New Email: "<<endl;
            cin >> b.email;
            cout << "Enter New Account Number: "<<endl;
            cin >> b.accountno;
            cout << "Enter New Account Type: "<<endl;
            
            cin >> b.accounttype;
            cout << "Enter New Balance: "<<endl;
            cin >> b.balance; 
        }
        temp << b.name << " " << b.address << " " << b.phone << " " << b.email << " "<< b.accountno << " " << b.accounttype << " " << b.balance << "\n";
    }
    file.close(); 
    temp.close(); 
    remove("Bank.txt");
    rename("Temp.txt", "Bank.txt");
}
int search_by_name(string name)     
{
    Bank b;
    ifstream infile;
    infile.open("Bank.txt");
    while (infile >> b.name >> b.address >> b.phone >> b.email >> b.accountno >> b.accounttype >> b.balance)
    {
        if (b.name == name)
        {
            cout << "Name: " << b.name << endl;
            cout << "Address: " << b.address << endl;
            cout << "Phone: " << b.phone << endl;
            cout << "Email: " << b.email << endl;
            cout << "Account Number: " << b.accountno << endl;
            cout << "Account Type: " << b.accounttype << endl;
            cout << "Balance: " << b.balance << endl;
            return 1;
        }
    }
    infile.close();
    return 0;
}
void display_all()   //display all accounts
{
    Bank b;
    ifstream infile;
    infile.open("Bank.txt");
    while (infile >> b.name >> b.address >> b.phone >> b.email >> b.accountno >> b.accounttype >> b.balance)
    {
        cout << "Name: " << b.name << endl;
        cout << "Address: " << b.address << endl;
        cout << "Phone: " << b.phone << endl;
        cout << "Email: " << b.email << endl;
        cout << "Account Number: " << b.accountno << endl;
        cout << "Account Type: " << b.accounttype << endl;
        cout << "Balance: " << b.balance << endl;
    }
    infile.close();
}
void delete_account(string name) 
{
    Bank b;
    ifstream infile;
    infile.open("Bank.txt");
    ofstream temp;
    temp.open("Temp.txt");
    while (infile >> b.name >> b.address >> b.phone >> b.email >> b.accountno >> b.accounttype >> b.balance)
    {
        if (b.name != name)
        {
            temp << b.name << " " << b.address << " " << b.phone << " "<< b.email << " " << b.accountno << " " << b.accounttype << " " << b.balance << "\n";
        }
    }
    infile.close();     
    temp.close();
    remove("Bank.txt");
    rename("Temp.txt", "Bank.txt");
}
int main()
{
    int choice;   
    string name;
    double amount;

    do
    {
        cout << "Enter Your Choice: " << endl;
        cout << "1. Create Account" << endl;
        cout << "2. Display Account" << endl;
        cout << "3. Modify Account" << endl;
        cout << "4. Search Account" << endl;
        cout << "5. Display All Accounts" << endl;
        cout << "6. Delete Account" << endl;
        cout << "7. Deposit" << endl;
        cout << "8. Withdraw" << endl;
        cout << "9. Balance Inquiry" << endl;
        cout << "10. Exit" << endl;
        cin >> choice;
        switch (choice)
        {
        case 1:
            create_account();
            break;
        case 2:   
            display_account();
            break;      
        case 3:
            cout << "Enter The Name You Want To Modify: "<<endl;
            cin >> name;
            modify_account(name, " ");
            break;
        case 4:
            cout << "Enter The Name You Want To Search: "<<endl;
            cin >> name;
            search_by_name(name);
            break;
        case 5:
            display_all();
            break;
        case 6:
            cout << "Enter The Name You Want To Delete: "<<endl;
            cin >> name;
            delete_account(name);
            break;
        case 7:
            cout << "Enter The Name You Want To Deposit: " << endl;
            cin >> name;
            cout << "Enter The Amount You Want To Deposit: " << endl;
            cin >> amount;
            deposit(name, amount);
            break;
        case 8:
            cout << "Enter The Name You Want To Withdraw: " << endl;
            cin >> name;
            cout << "Enter The Amount You Want To Withdraw: " << endl;
            cin >> amount;
            withdraw(name, amount);
            break;
            default :
        case 9:
            exit(0);
            break;
        default :
            cout << "Invalid Choice" << endl;
        }
    } while (choice != 7);
    return 0;
}
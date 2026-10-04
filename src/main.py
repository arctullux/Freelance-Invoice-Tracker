# Small invoice tracker for freelancers.

import sqlite3

dbConnection = sqlite3.connect("../db/invoices.db")
dbCursor = dbConnection.cursor()

# invoice ID format: I2026-00X
def createInvoice():
    print("I am going to need some information.")
    name = input("What is the client's name? > ")
    affiliation = input("What company or organization is the client affiliated with? > ")
    services = input("What were the services rendered? > ")
    due_date = input("What is the due date? (mm/dd/yyyy) > ")
    date_issued = input("What was the date issued? (mm/dd/yyyy) > ")
    client_phone_number = input("Whats the client's phone number? > ")
    client_email_address = input("Whats the client's email address? > ")
    client_billing_address = input("Whats the client's billing address? > ")
    invoice_status = input("What is the status? (new/upcoming/paid/overdue) > ")
    
    amount_due = input("What is the amount due? ($x.xx) > ")
    services = input("What services were/will be rendered? > ")
    
    print(
        f"""
        Name: {name}\n
        Affiliation: {affiliation}\n
        Services: {services}\n
        Due Date: {due_date}\n
        Issued: {date_issued}\n
        Client Phone Number: {client_phone_number}\n
        Client Email Address: {client_email_address}\n
        Client Billing Address: {client_billing_address}\n
        Invoice Status: {invoice_status}\n
        Amount Due: {amount_due}\n
        Services Issued: {services}\n
        """

    )
    
def deleteInvoice(invoiceID):
    pass
    
def editInvoice(invoiceID):
    pass

def printMenu():
    print("""Welcome to the Invoice Tracker. How can I be of assistance?
        1) Create an Invoice
        2) Delete an Invoice (Invoice ID required)
        3) Edit an Invoice (Invoice ID required)
        4) Exit
        """)
def main():
    choice = None
    while choice != "4":
        choice = input("Choose an option from 1 - 4. > ")
        match choice:
            case "1":
                createInvoice()
            case "2":
                print("Delete an invoice.")
            case "3":
                print("Edit an invoice.")
            # case "c":
                # dbCursor.execute("""CREATE TABLE IF NOT EXISTS Invoice (
                    # InvoiceID TEXT,
                    # fullName TEXT,
                    # affiliation TEXT,
                    # services TEXT,
                    # dueDate TEXT,
                    # dateIssued TEXT,
                    # clientPhoneNumber TEXT,
                    # clientEmailAddress TEXT,
                    # clientBillingAddess TEXT,
                    # invoiceStatus TEXT,
                    # taxRequired TEXT,
                    # otherFees TEXT,
                    # totalAmountDue TEXT,
                    # amountTendered TEXT,
                    # paymentMethod TEXT
                    # otherAmountTendered TEXT,
                    # otherPayment TEXT
                # )""")
            case "4":
                print("Goodbye.")
                break
            case _:
                print("That is not a valid option.")
    
if __name__ == "__main__":
    main()

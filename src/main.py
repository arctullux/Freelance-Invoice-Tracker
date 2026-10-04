# Small invoice tracker for freelancers.

import sqlite3
from datetime import datetime
import re
dbConnection = sqlite3.connect("../db/invoices.db")
dbCursor = dbConnection.cursor()

# invoice ID format: I2026-00X
def createInvoice():
    print("""Client information and freelancer information will be needed to create an invoice.
             Please gather and enter the following information below the line:
             
             Name (Full name, excluding middle initial)
             Affiliation
             Due Date
             Date Issued
             Client Phone Number (Optional, if email is included. Include country code, and separate blocks of numbers.)
             Client Email Address (Optional, if phone number is included.)
             Client Billing Address (Address of business, typically)
             Invoice Status (Please include one of 4 options: New, Incoming, Paid, or Overdue.)
             Amount Due (Include currency units, and include two decimal places.)
             Services (What services were rendered? Be detailed.)
             
             =======================================================================
             """)

    # TODO: Validate input with regular expressions.
    name = input("What is the client's name? > ")
    affiliation = input("What company or organization is the client affiliated with? > ")
    while True:
        due_date = input("What is the due date? (mm/dd/yyyy) > ")
        valid = validateTheDate(due_date)
        if valid:
            break
        else:
            print("That is not a valid date.")
            continue
    while True:
        date_issued = input("What was the date issued? (mm/dd/yyyy) > ")
        valid = validateTheDate(date_issued)
        if valid:
            break
        else:
            print("That is not a valid date.")
            continue
    client_phone_number = input("Whats the client's phone number? > ")
    client_email_address = input("Whats the client's email address? > ")
    client_billing_address = input("Whats the client's billing address? > ")
    while True:
        invoice_status = input("What is the status? (new/upcoming/paid/overdue) > ")
        match invoice_status:
            case "new":
                break
            case "upcoming":
                break
            case "paid":
                break
            case "overdue":
                break
            case _:
                print("That is not a valid status.")

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

def validateTheDate(date):
    try:
        datetime.strptime(date, "%mm/%dd/%YYYY")
        return True
    except ValueError:
        return False
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

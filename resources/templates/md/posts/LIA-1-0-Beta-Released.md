{:layout :post
:title  "LIA 1.0 Beta Released"
:date "2017-04-17"
:author "Ryan Himmelwright"
:tags ["Dev" "Solus" "Python" "Ledger"]
:draft? False
}

I have released the 1.0 Beta version for a personal project of mine, the **L**edger **I**mport **A**ssistant, or [LIA](https://github.com/himmALlRight/LIA/). This post will talk a bit about the the background of this project. I will also briefly explain what the beta release means, and what my future plans for the project are.

<!-- more -->

## What is LIA?

![Credit Card Statement CSV](../../img/posts/LIA-1-0-Beta-Released/creditCardDownload.png)

A while ago, I learned about [Ledger](http://www.ledger-cli.org), the command line double-entry accounting application, and wanted to start keeping tack of our finances with it. I wanted easily import our bank and credit card statements into ledger journals, and then use ledger to analyze the finances. However, there was one issue. While there are several other great ledger convert/import options out there, many were more complicated than what I was looking for. So...I decided to write my own tool. 

![Example Ledger Journal File](../../img/posts/LIA-1-0-Beta-Released/ledger-journal.png)

*Example Ledger Journal File*

When I started writing LIA, I just wanted a python script that could help me convert the contents of a .csv file into a ledger-journal formatted file (without any of the fancy features. Just the basics). I thought it was a simple task that should only take me a few hours. And it did. I wrote the the first basic implementation of LIA on a Sunday afternoon. However, while coding that bare-bones version, I realized while it *technically worked*, it would not be enjoyable to use, and therefore I would never use it. So I decided to expand it into something more than a script.


## What does LIA do?

![LIA Running](../../img/posts/LIA-1-0-Beta-Released/LIA-demo.gif)

LIA does the basic core functionality that originally prompted me to write it: converting bank/credit card statement csv files into ledger journal files. However, it has a few nice features that help the user manually convert these files in an enjoyable way. By going through each transaction manually, the user has full control to make sure data is being input correctly. However, LIA helps make the otherwise dull process fast and efficient. Some of the features that help LIA accomplish this are:

- CSV files are read in and converted to simple ledger journal statements.
- Data order is recognized by a header mechanism
- Prompts the user to potentially edit the transaction information (defaults to csv value)
- Manual transaction entry (if desired)
- Supports multiple destination accounts
- Automatic placement system. The user can specify a file containing rules to automatically place transactions. (ex: anything with "Dunkin" in the description will default to Expenses:Food:Coffee)
- Colored prompts



## What does LIA 1.0 Beta mean?
### LIA 1.0
When I realized LIA would be a good personal project beyond a script, I thought of several features that would make converting CSV statements much easier, and got to work. I worked on the project here and there, adding each feature over time. These features are what I determined were required in order for the application to be acceptably *usable*. I decided when all of those requirements were met, I would release an official 1.0 Branch.

The main functionality of LIA has been implemented for a while now. Being a python application, it has been possible to run LIA by calling the files with python. However, I didn't want to realse the 1.0 version because I hadn't finished making an installer so that LIA could be run like a normal linux application. I have now finished the `setup.py` file, so users can use python's setuptools to install LIA as an application on their computer. Additionally, I have even packaged LIA as a Solus eopkg. So it looks like I am ready for release.

### Beta
Sort of. Until now, I have been developing but not using LIA day to day. I want to spend some time actually *using* the application to see if there are any remaining issues. Additionaly, I have not confirmed that it fully does what is needed for ledger. So, I want to get a few ledger users to quickly look at it and let me know if they see any issues. After using it for awhile, and having others look at it, I will release it as the official 1.0 release. This will mean it should be stable enough for people to use, if they so choose to.

## Future Versions

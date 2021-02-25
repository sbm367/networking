# Python Networking Project

The purpose of this project is to learn basic netwokring in Python

The technologies covered in these examples are:

* TCP/IP Model
* Sockets
* urllib
* BeautifulSoup
* JSON & XML


## XML

* Tags
    start tags
    end tags
    self closing tags 
* Attributes
   Key, value
   values used double quotes "" 
* Serialize / Deserialize 

XML elements or nodes

XML as hierarchical or tree data 

Text data ismodeled as the child of thier tags

Attributes are also children of thier tags 

XML can also be read as paths:
a/b/c/ TEXT 

XML Standards

XML documents are governed by an XML Schema Contract.

An XML doc and schema are fed to a validator to determine if the doc is valid.

There are a number of different XML schema languages

XSD is the W3 standard XML Schema specification

XSD contains
* schema
* element
* sequence 
* complexType

Formated like 

<xs:{type}> 
for elements which have atributes and are self-closing 

Or like 
<xs:{type}> 
</xs:{type}> 

for complexType, sequence or schema

XSD also provides certain prebuilt types such as date and time and has feature to track counts as well as approved values. 

ISO 8601 Date/Time format is common in many web applications

{year-month-day}T{time of day, H:M:S}Z{timezone}
# Python Networking Project

The purpose of this project is to learn basic netwokring and web services in Python

The concepts & technologies covered in these examples are:

* TCP/IP Model
* Sockets
* urllib
* BeautifulSoup
* JSON & XML


# Networking

# Web Services 

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

## JSON

json is easy

[add notes, come back and clean this up later]

## Service Oriented Aproach

An app can't contain everything
Services publish rules applications must follow to make use of thier services, APIs

Have to interface between apps and apply standards to those interactions

## APIs

If we take the view opposite the sevice view, we are then building a web application using availible APIs

## Authentication

Acessing external APIs often requires the use of keys or tokens.  

Addtionaly, APIs are also often rate limited, allowing only a maximum number of requests over a time period. 

SOAP and REST are two common frameworks for designing APIs

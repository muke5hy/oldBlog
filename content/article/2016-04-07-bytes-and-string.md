Title: bytes and String 
Slug: bytes-and-string
Date: 2016-04-07 11:48:51
Tags: python, bytes
Category: programming
Author: mukesh
Lang: 
Status: draft
Summary: What is the difference between a string and a byte string?




The only thing that a computer can store is bytes.

To store anything in a computer, you must first encode it, i.e. convert it to bytes. For example:

    If you want to store music, you must first encode it using MP3, WAV, etc.
    If you want to store a picture, you must first encode it using PNG, JPEG, etc.
    If you want to store text, you must first encode it using ASCII, UTF-8, etc.

MP3, WAV, PNG, JPEG, ASCII and UTF-8 are examples of encodings. An encoding is a format to represent audio, images, text, etc in bytes.

In Python, a byte string is just that: a sequence of bytes. It isn't human-readable. Under the hood, everything must be converted to a byte string before it can be stored in a computer.

On the other hand, a character string, often just called a "string", is a sequence of characters. It is human-readable. A character string can't be directly stored in a computer, it has to be encoded first (converted into a byte string). There are multiple encodings through which a character string can be converted into a byte string, such as ASCII and UTF-8.

'I am a string'.encode('ASCII')

The above Python code will encode the string 'I am a string' using the encoding ASCII. The result of the above code will be a byte string. If you print it, Python will represent it as b'I am a string'. Remember, however, that byte strings aren't human-readable, it's just that Python decodes them to ASCII when you print them. In Python, a byte string is represented by a b, followed by the byte string's ASCII representation.

A byte string can be decoded back into a character string, if you know the encoding that was used to encode it.

b'I am a string'.decode('ASCII')

The above code will return the original string 'I am a string'.

Encoding and decoding are inverse operations. Everything must be encoded before it can be written to disk, and it must be decoded before it can be read by a human.

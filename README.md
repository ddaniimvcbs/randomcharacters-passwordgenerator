*WARNING* Because I used the "random" module, I recommend using these passwords only for social media and little else. Their algorithm (Mersenne Twister) is predictable. However, you can use the "secrets" library (I'll create a generator with that specific module later) which would be more secure.

First of all, thanks for taking a look at this. Perhaps it can help you learn something about Python; if so, I'm glad. I'm very new to programming, but I'll explain the reasoning behind all the code here, so you can also see if I understand what I'm programming.

Passwords are a fundamental part of protecting our credentials these days. Although methods like 2FA exist, we must always ensure that no one can know or guess our password by brute force (unless you're infected with an InfoStealer...).

I want to clarify that the code may be buggy, for example, by introducing a letter where the input variable for the password length is stored. As I learn about error exceptions, debugging, etc., I will fix it.

Introduction to the code:

How do we create this?

First, let's define a simple function without parameters. (I'm currently learning this in Python.)

Why without parameters?

We don't need them. Period. Although, for example, I could specify that it works with the "list" parameter.

By pure logic, we have to add either a single tuple with all the numbers, letters, and symbols, or create three tuples with numbers, letters, and symbols. I decided to do it this way to play around with "zip" and other things.

We could also use strings instead of tuples; everyone has their own idea.

Okay, now I've decided we need to limit the number of characters generated. If you only want a 25-character password, then it has to be 25 characters, and vice versa.


*ATTENTION*--- If you enter a VERY HIGH number of characters (something like 3948729047289), Python will crash.

Since I'm new, I can only deduce this without testing it in the script; I don't need to, as it's not very difficult to figure out.

We must create the variable "length" where we will store the number we ask the user for as their password character limit. We must use `int(input)`, since the user will enter an integer, and well, obviously, if we just use `input()`, Python will treat the data as a string (a little bit of English, let's see if we can improve too...).

Once this is done, we'll collect the maximum number of characters for the user's password.

Now, in my case, since the list is split into three parts, I've created a variable that groups the three variables into a single string (all_characters = numbers + letters + symbols).

Okay, now we'll use one of the first libraries I learned, along with time and maths: random.

I recommend this library as a first introduction.

So, obviously, we need to create another variable to store the action we'll give the library:

password = random.choices(all_characters, k=length)

This is where the "magic" happens (the function starts working, haha...(laughs)).

random.choices allows us to take elements from the single list we created with all_characters and generate the password.

But... where does k=length come from?

Well done... now you don't even know where "length" comes from, do you?

If you recall, we created a variable called length to store the maximum number of characters for the password... right? Do you remember? I hope so...

If we didn't set a variable for the length, and k were = 5, the password would be 5 CHARACTERS. k defines how many characters will be generated from the complete list; therefore, if the user doesn't set the number, the script will generate, for example, a password of 10, 15, or 20 characters every time.


Okay... so we have the password result. Now we create another variable to store the generated password and print it...

Let's execute the print statement. Let's make a 10-character password...

['_', 'b', 'b', '&', '|', '_', 'j', 'b', 'e', ​​'j']

Yeah, that's awful, what an ugly output...

Shall we fix it?

The `join` function has a very simple mission: to convert several elements from lists, tuples, etc., into a single string.

Well, it's simple: we create another variable, "password_list", and that's it.

Finally, we do a final print statement...

Password list!

This is the explained flow of my first script. I hope you like it!

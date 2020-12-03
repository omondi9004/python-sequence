#a program that turns a number of seconds into more human readable counts of hours, minutes, and seconds.
#A call to input() allows the user to enter the number of seconds. Then we convert that string to an integer.
#From there we use the division and modulus operators to compute the results.

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)


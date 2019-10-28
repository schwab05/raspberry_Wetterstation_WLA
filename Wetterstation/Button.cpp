#include <wiringPi.h>

#define buttonPin 0
#define ledPin 1




int main (void)
{
    pinMode(buttonPin, INPUT);
    pinMode(ledPin, OUTPUT);

    while(true)
    {
        if (buttonPin == 0)
        {
            digitalWrite(ledPin, HIGH);
        }
        else
        {
            digitalWrite(ledPin, LOW);
        }



    }

    return 0;





}


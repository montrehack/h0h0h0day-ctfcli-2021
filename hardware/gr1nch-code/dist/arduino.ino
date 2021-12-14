const char *MESSAGE = "JGTDOHCPQIUAQHKMRUBLNJMEULYEGEAXBTKZRRIMWXGUWDFMEJQAXWMJIILFGSZGWDWDYMTQNRREJIPIMQOCFSRBIBKZLJKMNGDGOKXWRUHQBELKP";
const char BASE_CHAR = 'A';
const int MESSAGE_LENGTH = strlen(MESSAGE);
const int BIT_OFFSET = 2;
const int BIT_COUNT = 5;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);

    for (int i = BIT_OFFSET; i < BIT_COUNT + BIT_OFFSET; i++) {
        pinMode(i, OUTPUT);
    }
}

void display_one(int bits) {
    for (int i = 0; i < BIT_COUNT; i++) {
        digitalWrite(i + BIT_OFFSET, (bits >> i) & 1);
    }
}

void display(const char *message, int length) {
    bool clock = false;
    for (const char *c = message; c < message + length; c++) {
        delay(1000);

        clock = !clock;
        digitalWrite(LED_BUILTIN, clock);

        display_one(*c - BASE_CHAR);
    }
}

void loop() {
    display(MESSAGE, MESSAGE_LENGTH);
    display_one(0);
    delay(5000);
}

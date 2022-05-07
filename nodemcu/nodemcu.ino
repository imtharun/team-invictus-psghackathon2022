#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>
#include <SPI.h>
#include <MFRC522.h>

const char *ssid =  "AMCS_IoT Lab";     // replace with your wifi ssid and wpa2 key
const char *pass =  "amcs@kla";

//Web/Server address to read/write from 
const char *host = "192.168.43.128";


constexpr uint8_t RST_PIN = D3;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = D4;     // Configurable, see typical pin layout above
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522::MIFARE_Key key;

WiFiClient client;

String tag;
 
void setup() 
{
       Serial.begin(9600);
       delay(10);
       Serial.begin(9600);
       SPI.begin(); // Init SPI bus
       rfid.PCD_Init(); // Init MFRC522
               
       Serial.println("Connecting to ");
       Serial.println(ssid); 
 
       WiFi.begin(ssid, pass); 
       while (WiFi.status() != WL_CONNECTED) 
          {
            delay(500);
            Serial.print(".");
          }
      Serial.println("");
      Serial.println("WiFi connected"); 
      Serial.println("IP address: ");
      Serial.println(WiFi.localIP());

      
}
 
void loop() 
{
  if ( ! rfid.PICC_IsNewCardPresent())
    return;
  if (rfid.PICC_ReadCardSerial()) {
    for (byte i = 0; i < 4; i++) {
      tag += rfid.uid.uidByte[i];
    }
    Serial.println(tag);
    tag = "";
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();

    String resp = senddata(tag);
    Serial.println(resp);
    
  }   
}

String senddata(String tag)
{
  
}

#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <string.h>

#define LCDAddr			0x27

#define INA219ADDR		0x40
#define INA219CONF		0x00
#define INA219SHUNTV	0x01
#define INA219BUSV		0x02
#define INA219POWER		0x03
#define INA219CURRENT	0x04
#define INA219CAL		0x05

int BLEN = 1;
int fd;

void write_word(int data){
	int temp = data;
	if ( BLEN == 1 )
		temp |= 0x08;
	else{
		temp &= 0xF7;
		printf("BLEN is not 1\n");
	}
	wiringPiI2CWrite(fd, temp);
}

void send_command(int comm){
	int buf;
	// Send bit7-4 firstly
	buf = comm & 0xF0;
	buf |= 0x04;			// RS = 0, RW = 0, EN = 1
	write_word(buf);
	delay(2);
	buf &= 0xFB;			// Make EN = 0
	write_word(buf);
	printf("send_command buf bit7-4 is %d\n", buf);
	delay(2000);

	// Send bit3-0 secondly
	buf = (comm & 0x0F) << 4;
	buf |= 0x04;			// RS = 0, RW = 0, EN = 1
	write_word(buf);
	delay(2);
	buf &= 0xFB;			// Make EN = 0
	write_word(buf);
	printf("send_command buf bit3-0 is %d\n", buf);
}

void send_data(int data){
	int buf;
	// Send bit7-4 firstly
	buf = data & 0xF0;
	buf |= 0x05;			// RS = 1, RW = 0, EN = 1
	write_word(buf);
	delay(2);
	buf &= 0xFB;			// Make EN = 0
	write_word(buf);
	printf("send_data buf bit7-4 is   %d\n", buf);
	delay(2000);


	// Send bit3-0 secondly
	buf = (data & 0x0F) << 4;
	buf |= 0x05;			// RS = 1, RW = 0, EN = 1
	write_word(buf);
	delay(2);
	buf &= 0xFB;			// Make EN = 0
	write_word(buf);
	printf("send_data buf bit3-0 is %d\n",buf);
}

void init(){
	send_command(0x33);	// Must initialize to 8-line mode at first
	delay(5);
	send_command(0x32);	// Then initialize to 4-line mode
	delay(5);
	send_command(0x28);	// 2 Lines & 5*7 dots
	delay(5);
	send_command(0x0C);	// Enable display without cursor
	delay(5);
	send_command(0x01);	// Clear Screen
	wiringPiI2CWrite(fd, 0x08);
}

void clear(){
	send_command(0x01);	//clear Screen
}

void write(int x, int y, char data[]){
	int addr, i;
	int tmp;
	if (x < 0)  x = 0;
	if (x > 15) x = 15;
	if (y < 0)  y = 0;
	if (y > 1)  y = 1;

	// Move cursor
	addr = 0x80 + 0x40 * y + x;
	send_command(addr);
	
	tmp = strlen(data);
	for (i = 0; i < tmp; i++){
		send_data(data[i]);
//		wiringPiI2CWrite(fd, data[i]);
		printf("Now   %c   is printed\n", data[i]);
	}
}


void main(){
	fd = wiringPiI2CSetup(LCDAddr);
	init();
	char str[100];
	int data = 100;
	//delay(2000);
	clear();
	while (1)
	{
		write(0, 0, "A1 B2!");
		sprintf(str, "%d", data)
		write(1, 4, "");
	}
	
}



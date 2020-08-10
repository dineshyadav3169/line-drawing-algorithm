# Line Drawing Algorithm
In computer graphics, a digital differential analyzer (DDA) is hardware or software used for interpolation of variables over an interval between start and end point. DDAs are used for rasterization of lines, triangles and polygons. They can be extended to non linear functions, such as perspective correct texture mapping, quadratic curves, and traversing voxels.
<br><br>
The DDA method can be implemented using floating-point or integer arithmetic. The native floating-point implementation requires one addition and one rounding operation per interpolated value (e.g. coordinate x, y, depth, color component etc.) and output result. This process is only efficient when an FPU with fast add and rounding operation will be available.
The fixed-point integer operation requires two additions per output cycle, and in case of fractional part overflow, one additional increment and subtraction. The probability of fractional part overflows is proportional to the ratio m of the interpolated start/end values.
DDAs are well suited for hardware implementation and can be pipelined for maximized throughput.


## DDA algorithm Program in Turbo C++:
```
#include <graphics.h>

#include <iostream.h>
#include <math.h>
#include <dos.h>
#include <conio.h>

void main( )
{
  float x, y, x1, y1, x2, y2, dx, dy, step;
  int i, gd = DETECT, gm;
  initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
  
  cout << "Enter the value of x1 and y1 : ";
  cin >> x1 >> y1;
  cout << "Enter the value of x2 and y2: ";
  cin >> x2 >> y2;
  
  dx = (x2 - x1);
  dy = (y2 - y1);
  if (abs(dx) >= abs(dy))
    step = abs(dx);
  else
    step = abs(dy);
  dx = dx / step;
  dy = dy / step;
  x = x1;
  y = y1;
  i = 1;
  while (i <= step) {
    putpixel(x, y, 5);
    x = x + dx;
    y = y + dy;
    i = i + 1;
    delay(100);
  }
  getch();
  closegraph();
}
```

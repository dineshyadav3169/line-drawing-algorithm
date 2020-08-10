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
# Bresenham's line algorithm

Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points. It is commonly used to draw line primitives in a bitmap image (e.g. on a computer screen), as it uses only integer addition, subtraction and bit shifting, all of which are very cheap operations in standard computer architectures. It is an incremental error algorithm. It is one of the earliest algorithms developed in the field of computer graphics. An extension to the original algorithm may be used for drawing circles.
<br>
While algorithms such as Wu's algorithm are also frequently used in modern computer graphics because they can support antialiasing, the speed and simplicity of Bresenham's line algorithm means that it is still important. The algorithm is used in hardware such as plotters and in the graphics chips of modern graphics cards. It can also be found in many software graphics libraries. Because the algorithm is very simple, it is often implemented in either the firmware or the graphics hardware of modern graphics cards.

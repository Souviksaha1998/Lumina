
# Lumina 🚀
#### With Lumina, you can customize object bounding boxes for better visualization and create zones for more efficient tracking.

<!-- <img src='images\logo1.png'> -->
![Sample Image](https://drive.google.com/uc?export=view&id=1vgHqqxXDYc7Vs3esV-zHUdqVpc6jw6jI)

## Output from Lumina 

![Sample Image](https://drive.google.com/uc?export=view&id=1hcuxS4mYhyu1B2q4bR_Tl_lFPc3jInF_)

##  How to use Lumina❓
#### Install the module first using pip 🚀

```python
pip install lumina

```
#### For Github clone 🚀
Github clone link : [Lumina](https://github.com/Souviksaha1998/Lumina) repo 🖥️

## After Installation, Import the Lumina class  🚀

```python
# create a .py file
# import modules
from Lumina.lumina import Lumina
from Lumina.colors import color_palette
# create a object of lumina 
lumina = Lumina()
#if you want color palette then do this, it will return random colors
color = color_palette() 
```
## Usage (Functions of lumina)🎯
#### you can use this functions by - (lumina.<function_name>)
![Sample Image](https://drive.google.com/uc?export=view&id=1bC4RMZ8Y7PNIIA9D6lLb639HHytknx1x)
![Sample Image](https://drive.google.com/uc?export=view&id=1_tBuBeHIBfE5QIEVO14YRp5lytDoNhjD)
![Sample Image](https://drive.google.com/uc?export=view&id=1dsKn7QlFXlZF4OwCF5c_tt4QD0iUrKLJ)
![Sample Image](https://drive.google.com/uc?export=view&id=1SfevAAWo-RwccIgpjBV9hKrwxfR0tPIu)

***
## 1.1 Polygon zone creation for detection or tracking
### This function will create a polygon zone.
<img src='images\ex5.png'>

## 1.2 polygon_in_out_counter function will create polygon region and return image and bool = True , if anything is inside in the poly region. -- this function is helpful for region based tracking. Alternatively You can use line_in_out_counter

![Sample Image](https://drive.google.com/uc?export=view&id=1ffycsUaZkWp1vxgLpoeqnGd5weqbaiz4)

## 1.3 This function will create a mask, based on points. If you don't want to capture the whole frame then you can use this function. This will reduce computational cost.

![Sample Image](https://drive.google.com/uc?export=view&id=1gDZTPiZeJPvtWrI8oY2be3SP4Zfq_PAt)


### It is my goal to constantly improve Lumina, and these are some of the initial features. I will be adding more features to better customize Lumina in the future. Thanks in advance. :)

***

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)



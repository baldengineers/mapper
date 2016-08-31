class Create():
    def __init__(self, vmf_file, prefab_name, prefab_text, prefab_icon, workshop_export,indexLine,index):
        #vmf_file | string | contains the filepath of the vmf file of the prefab
        #prefab_name | string | is the filename of the prefab file being created
        #prefab_text | string | is the name of the prefab as it will appear in the main application window
        #prefab_icon | string | is the filepath of the icon of the prefab as it will appear in the main application window
        #workshop_export | boolean | that determines whether the prefab will be zipped for export to the workshop
        #indexLine |  | I have no fucking idea
        #index |  | I have no idea about this either

        self.LEVEL_HEIGHT = 448 #self.LEVEL_HEIGHT is the constant for the height of each level of the map.
        self.var_list = [] #self.var_list contains all the variables needed to be written to the prefab.py file
        self.var_num = 1 #self.var_num is the number that appears after the variable. ex. (x1 y1 z1) (x2 y2 z2) (x3 y3 z3)
        self.compile_list = [ #self.compilelist is the outline of the prefab.py file
        """import os
import math
def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point
def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list, rotation, level):

    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
""",

  "#INSERT_OPEN_FILE\n",

  """
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
""",

  "#INSERT_PY_LIST\n",

  "#INSERT_VAR_COUNT\n",

  """
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    normal_list,axislist,negaxislist,vaxis,uaxis=[],['1 0 0 1','0 1 0 1','0 0 1 1'],['-1 0 0 1','0 -1 0 1','0 0 -1 1'],0,0
    def evaluate(coords):
        dist_x,dist_y,dist_z = abs(coords[0]),abs(coords[1]),abs(coords[2]),
        if dist_x >= dist_y and dist_x >= dist_z:
            return axislist[0]
        if dist_y >= dist_z:
            return axislist[1]
        return axislist[2]
    def get_normal(coord_list):
        vector_a = (coord_list[1][0]-coord_list[0][0],coord_list[1][1]-coord_list[0][1],coord_list[1][2]-coord_list[0][2])
        vector_b = (coord_list[2][0]-coord_list[0][0],coord_list[2][1]-coord_list[0][1],coord_list[2][2]-coord_list[0][2])

        normal = (vector_a[1]*vector_b[2]-vector_a[2]*vector_b[1],vector_a[2]*vector_b[0]-vector_a[0]*vector_b[2],vector_a[0]*vector_b[1]-vector_a[1]*vector_b[0])
        return normal

    for normal_num in range(1,var_count+1,3):
        normal_list=[]
        for i in range(3):
            normal_list.append([])
            for var in ["x", "y", "z"]:
                normal_list[i].append(eval(var+str(normal_num+i)))
        coords = get_normal(normal_list)
        response = evaluate(coords)
        if response == axislist[0]:
            uaxis = axislist[1]
        else:
            uaxis = axislist[0]
        if response == axislist[2]:
            vaxis = negaxislist[1]
        else:
            vaxis = negaxislist[2]
        values = values.replace('AXIS_REPLACE_U',uaxis,1)
        values = values.replace('AXIS_REPLACE_V',vaxis,1)

    for i in range(ogvalues.count("world_idnum")):
        values = values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1

    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))
            if var == "z":
                values = values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
            else:
                values = values.replace(string + " ",string_var + " ")
    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
        if "ROTATION_RIGHT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_RIGHT","0 0 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_RIGHT","0 270 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_RIGHT","0 180 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_RIGHT","0 90 0",1)
        if "ROTATION_UP" in values:
            if rotation == 0:
                values = values.replace("ROTATION_UP","0 90 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_UP","0 0 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_UP","0 270 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_UP","0 180 0",1)
        if "ROTATION_LEFT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_LEFT","0 180 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_LEFT","0 90 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_LEFT","0 0 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_LEFT","0 270 0",1)
        if "ROTATION_DOWN" in values:
            if rotation == 0:
                values = values.replace("ROTATION_DOWN","0 270 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_DOWN","0 180 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_DOWN","0 90 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_DOWN","0 0 0",1)
    values = values.replace('"[0 0 0 1] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 0 1 0] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 1 0 0] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[1 0 0 0] 0.25"','"[1 1 1 1] 0.25"')
        """,

        "#INSERT_ENT_CODE\n",]

        block_type = "" #block_type contains the current block of code the program is currently looking at. A block of code is determined by the two brackets {}/()/[] surrounding it.
        
        with open(vmf_file, "r") as f:
            vmf_data = f.readlines()
            header = True

            for index, line in enumerate(vmf_data):
                if "solid" in line:
                    if header:
                        header = False
                        vmf_data[:index] = ""
                    block_type = "solid"
                elif "side" in line:
                    block_type = "side"
                elif "id" in line:
                    if block_type == "solid":
                        id_var = "world_idnum"
                    elif block_type == "side":
                        id_var = "id_num"
                    vmf_data[index] = vmf_data[:vmf_data[index].index("id")+5] + id_var + "\"" #This line does this: "id" " + id_var + "
                elif "(" in line:
                    if block_type == "side":
                        for char in line:
                            if char == "(":
                                num = ["","",""] #num is for the numbers in the parenthesis that are the points for the plane, it is a list of STRINGS
                                num_index = 0 #current index for the num variable above
                                block_type = "()"
                            elif block_type = "()":
                                if not char == " ":
                                    if not char == ")":
                                        num[num_index] += char
                                    else:
                                        self.assign_var(num)
                                else:
                                    index += 1
    def assign_var(self, num):
        #assigns values for the variables (x1,y1,z1,x2,etc...) and writes them to self.var_list
        xyz_list = ["x","y","z"]
        
        """for index, var in enumerate(xyz_list):
            if var == "z":
                text = "%s%d = level*%d + %d" %(var, self.var_num, LEVEL_HEIGHT, num[index])
            else:
                text = "%s%d = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*%d*512%s%s, posy*%d*512%s%s), (360 if rotation!=0 else 0)-90*rotation)[%d])" %(var, var_num, num[index], py_list[-2][py_list[-1].index("=") + 2:], 0 if var == "x" or var == "px" else 1)
                #change so it assigns a variable to this whole thing, then find the index
                #plz change the above and make it also work for 0 by removing the thing at end if value == 0. Also implement the negative- positive for x and negative for y
            self.var_list.append(text)"""
            
        self.var_list.append("%s%d = level*%d + %d" %(var, self.var_num, LEVEL_HEIGHT, num[index]))
        self.var_list.append("xy%d = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*%d*512%s%s, posy*%d*512%s%s), (360 if rotation!=0 else 0)-90*rotation)[%d])" %(var, var_num, num[index], py_list[-2][py_list[-1].index("=") + 2:], 0 if var == "x" or var == "px" else 1))
        
        for var in ["x","y"]:
            self.var_list.append("%s%d = xy%d[%s]" %(var, self.var_num, self.var_num, 0 if var == "x" else 1))
            
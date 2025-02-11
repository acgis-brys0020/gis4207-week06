

import os
import sys



def main():

    global arcpy, env
    if len(sys.argv) !=4:
        print("data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>")


    import arcpy
    from arcpy import env

    in_gdbs_base_folder = sys.argv[1]

    out_gdb = sys.argv[2]

    out_feature_datset = sys.argv[3]

    UTM_10_dataprep(in_gdbs_base_folder, out_gdb, out_feature_datset)


def UTM_10_dataprep(in_gdbs_base_folder, out_gdb, out_feature_dataset):
    arcpy.env.workspace = in_gdbs_base_folder
    arcpy.ListWorkspaces(in_gdbs_base_folder)

    out_folder_path = os.path.dirname(out_gdb)
    arcpy.management.CreateFileGDB(out_folder_path, os.path.basename(out_gdb))



    Surrey_Working_gdb = arcpy.management.CreateFileGDB(out_folder_path, out_name=out_gdb)
    



if __name__ == '__main__':
    main()





    





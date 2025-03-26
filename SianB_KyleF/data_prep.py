

import os
import sys



def main():

#usage and script arugments 
    global arcpy, env
    if len(sys.argv) != 4:
        print("data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>")
        sys.exit()
        


    import arcpy
    from arcpy import env

    in_gdbs_base_folder = sys.argv[1]

    out_gdb = sys.argv[2]

    out_feature_datset = sys.argv[3]

    UTM_10_dataprep(in_gdbs_base_folder, out_gdb, out_feature_datset)


#function to move feature classes into feature dataset with defined projection 
def UTM_10_dataprep(in_gdbs_base_folder, out_gdb, out_feature_dataset):
    
    env.workspace = in_gdbs_base_folder
    gdb_list = arcpy.ListWorkspaces(workspace_type="FileGDB")


    if not gdb_list:
        print("No geodatabases found in the input folder.")
        sys.exit(1)

    out_folder_path = os.path.dirname(out_gdb)

   
    if not arcpy.Exists(out_gdb):
        arcpy.management.CreateFileGDB(out_folder_path, os.path.basename(out_gdb))

#getting and setting the spatial reference 
    spatial_ref = None
    for gdb in gdb_list:
        env.workspace = gdb
        feature_classes = arcpy.ListFeatureClasses()
        if feature_classes:
            desc = arcpy.Describe(os.path.join(gdb, feature_classes[0]))
            spatial_ref = desc.spatialReference

    if not spatial_ref:
        print("No feature classes found in any geodatabases.")
        sys.exit(1)


    out_fds = os.path.join(out_gdb, out_feature_dataset)
    if not arcpy.Exists(out_fds):
        arcpy.management.CreateFeatureDataset(out_gdb, out_feature_dataset, spatial_reference=spatial_ref)

#copy features into dataset
    for gdb in gdb_list:
        env.workspace = gdb
        for fc in arcpy.ListFeatureClasses():
            arcpy.management.CopyFeatures(os.path.join(gdb, fc), os.path.join(out_fds, fc))
            print(f"Copied {fc} from {gdb} to {out_fds}")


if __name__ == '__main__':
    main()





    





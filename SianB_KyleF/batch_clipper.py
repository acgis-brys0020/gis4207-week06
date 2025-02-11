import os
import sys

def main():
    """Clips all feature classes in Sites to the shapefiles from TargetData."""
    global arcpy, env
    if len(sys.argv) !=4:
        print("Usage:  batch_clipper.py <InWorkspace> <ClipWorkspace> <OutputWorkspace>")
        sys.exit()

    import arcpy
    from arcpy import env    

    in_ws = sys.argv[1]
    if not arcpy.Exists(in_ws):
        print(in_ws, "does not exist")
        sys.exit()

    clip_ws = sys.argv[2]
    if not arcpy.Exists(clip_ws):
        print(in_ws, "does not exist")
        sys.exit()

    out_ws = sys.argv[3]
    if not arcpy.Exists(out_ws):
        print(in_ws, "does not exist")
        sys.exit()

    batch_clipper(in_ws, clip_ws, out_ws)

def batch_clipper(in_ws, clip_ws, out_ws):
    arcpy.env.overwriteOutput = True 
    arcpy.env.workspace = in_ws
    for in_fc in arcpy.ListFeatureClasses():
        in_path = os.path.join(in_ws, in_fc)
        arcpy.env.workspace = clip_ws
        for clip_fc in arcpy.ListFeatureClasses():
            clip_path = os.path.join(clip_ws, clip_fc)
            out_fc = f'{clip_fc[:-4]}_{in_fc}'
            out_fc_path = os.path.join(out_ws, out_fc)
            arcpy.Clip_analysis(in_path, clip_path, out_fc_path)


if __name__ == '__main__':
    main()

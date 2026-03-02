class CubeSolver:
  def __init__():
    faces={'blue','green','orange','red','yellow','white'}
    mutually_oppsite_side_phases={'blue':'green','orange':'red','yellow':'white'}
    colors={'blue','green','orange','red','yellow','white'}
    vertex=
    {
      "rgy":["red","green","yellow"],
      "rgw":["red","green","white"],
      "rby":["red","blue","yellow"],
      "rbw":["red","blue","white"],
      "ogy":["orange","green","yellow"],
      "ogw":["orange","green","white"],
      "oby":["orange","blue","yellow"],
      "obw":["orange","blue","white"]
    }
    edges=
    {
      "rb":["red","blue"],
      "rg":["red","green"],
      "rw":["red","white"],
      "ry":["red","yellow"],
      "ob":["orange","blue"],
      "og":["orange","green"],
      "ow":["orange","white"],
      "oy":["orange","yellow"],
      "by":["blue","yellow"],
      "bw":["blue","white"],
      "gw":["green","white"],
      "gy":["green","yellow"]
    }
    states=
    move_paths=
    solution={
      "rgy":"rgy",
      "rgw":"rgw",
      "rby":"rby",
      "rbw":"rbw",
      "ogy":"ogy",
      "ogw":"ogw",
      "oby":"oby",
      "obw":"obw"
    }
  def solver():
      batch=27
      block=20
      epoches=20
      for epoch in range(epoches):
        
  def moves():
      state=solver()
      while state!=solution:
        moves()

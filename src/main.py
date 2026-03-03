class CubeSolver:
  def __init__():
    faces={'b':'blue','g':'green','o':'orange','r':'red','y':'yellow','w':'white'}
    mutually_oppsite_side_faces={'blue':'green','orange':'red','yellow':'white'}
    mosf={'b':'g','g':'b','o':'r','r':'o','y':'w','w':'y'}
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
    states={}
    move_paths={"rgy","rgw","rgo","rby","rbw","rbo","grw","gry","grb","gow","goy","gob","yrg","yrb","yrw","yog","yob","yow"}
    solution={
      "rgy":"rgy",
      "rgw":"rgw",
      "rby":"rby",
      "rbw":"rbw",
      "ogy":"ogy",
      "ogw":"ogw",
      "oby":"oby",
      "obw":"obw",
      "rb":"rb",
      "rg":"rg",
      "rw":"rw",
      "ry":"ry",
      "ob":"ob",
      "og":"og",
      "ow":"ow",
      "oy":"oy",
      "by":"by",
      "bw":"bw",
      "gw":"gw",
      "gy":"gy"
    }
    state_given={
      "rgy":"ogw",
      "rgw":"ybo",
      "rby":"ryg",
      "rbw":"bwr",
      "ogy":"yrb",
      "ogw":"oyg",
      "oby":"owb",
      "obw":"wrg",
      "rb":"gy",
      "rg":"rw",
      "rw":"yr",
      "ry":"by",
      "ob":"gw",
      "og":"bw",
      "ow":"oy",
      "oy":"ow",
      "by":"go",
      "bw":"rb",
      "gw":"ob",
      "gy":"gr"
    }
  def next_moves(last_move):
    moves={}
    for m in range(18):
      if(last_move.strip()[:2]!=move_paths[m].strip()[:2]):
        moves[m]=move_paths[m]
    return moves
  def mover(moving_step,state):
    f=moving_step.strip()[0]
    s=moving_step.strip()[1]
    c=moving_step.strip()[2]
    s1=f
    s2=mosf[f]
    s3=c
    s4=mosf[c]
    # mosf[f] mosf[s]
    moving_block={}
    moving_block.append{f"{f}{s}{c}",f"{f}{s}{mosf[c]}",f"{mosf[f]}{s}{c}",f"{mosf[f]}{s}{mosf[c]}",f"{f}{s}",f"{s}{c}",f"{mosf[f]}{s}",f"{s}{mosf[c]}"}
    if mosf[f]!=c:
      # moving_block={}
      # moving_block.append{f"{f}{s}{c}",f"{f}{s}{mosf[c]}",f"{mosf[f]}{s}{c}",f"{mosf[f]}{s}{mosf[c]}",f"{f}{s}",f"{s}{c}",f"{mosf[f]}{s}",f"{s}{mosf[c]}"}
      for name in moving_block:
        if any(sorted(name) == sorted (state_element) for state_element in state):
    
    elif mosf[f]==c:
      # moving_block={f s c,f s mosf[c],mosf[f] s c, mosf[f] s mosf[c],f s, s c , mosf[f] s, s mosf[c]}
    
    return state
  def solver():
      batch=27
      block=20
      epoches=20
      for epoch in range(epoches):
        
  def moves(state, move_list=move_paths):
      moves_to=move_list
      cur_state=state
      i=0
      # states = {}
      while state!=solution:
        states[i] = web_url
        last_move=moves_to[i]
        next_move={}
        for to_move in moves_to:
          if last_move != to_move:
            next_move.append(to_move)
        i=i+1
        moves(cur_state,next_move)
if __name__=="__main__":
  cs=CubeSolver()
  cs.moves

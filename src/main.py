import json

class CubeSolver:
  move_paths={"rgy","rgw","rgo","rby","rbw","rbo","grw","gry","grb","gow","goy","gob","yrg","yrb","yrw","yog","yob","yow"}
  def __init__(self):
    self.output_file="./puzzle_move_and_states.json"
    faces={'b':'blue','g':'green','o':'orange','r':'red','y':'yellow','w':'white'}
    mutually_oppsite_side_faces={'blue':'green','orange':'red','yellow':'white'}
    self.mosf={'b':'g','g':'b','o':'r','r':'o','y':'w','w':'y'}
    colors={'blue','green','orange','red','yellow','white'}
    # self.move_paths={"rgy","rgw","rgo","rby","rbw","rbo","grw","gry","grb","gow","goy","gob","yrg","yrb","yrw","yog","yob","yow"}
    vertex={
      "rgy":["red","green","yellow"],
      "rgw":["red","green","white"],
      "rby":["red","blue","yellow"],
      "rbw":["red","blue","white"],
      "ogy":["orange","green","yellow"],
      "ogw":["orange","green","white"],
      "oby":["orange","blue","yellow"],
      "obw":["orange","blue","white"]
    }
    edges={
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
    # states={}
    self.solution={
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
  def mover(self,moving_step,state):
    f=moving_step.strip()[0]
    s=moving_step.strip()[1]
    c=moving_step.strip()[2]
    s1=f
    s2=self.mosf[f]
    s3=c
    s4=self.mosf[c]
    # mosf[f] mosf[s]
    moving_block=[]
    mb={}
    # moving_block.append(f"{f}{s}{c}",f"{f}{s}{self.mosf[c]}",f"{self.mosf[f]}{s}{c}",f"{self.mosf[f]}{s}{self.mosf[c]}",f"{f}{s}",f"{s}{c}",f"{self.mosf[f]}{s}",f"{s}{self.mosf[c]}")
    moving_block.append(f"{f}{s}{c}")
    moving_block.append(f"{f}{s}{self.mosf[c]}")
    moving_block.append(f"{self.mosf[f]}{s}{c}")
    moving_block.append(f"{self.mosf[f]}{s}{self.mosf[c]}")
    moving_block.append(f"{f}{s}")
    moving_block.append(f"{s}{c}")
    moving_block.append(f"{self.mosf[f]}{s}")
    moving_block.append(f"{s}{self.mosf[c]}")
    # if self.mosf[f]!=c:
    # moving_block={}
    # moving_block.append{f"{f}{s}{c}",f"{f}{s}{mosf[c]}",f"{mosf[f]}{s}{c}",f"{mosf[f]}{s}{mosf[c]}",f"{f}{s}",f"{s}{c}",f"{mosf[f]}{s}",f"{s}{mosf[c]}"}
    for name in moving_block:
      print(f"={name}")
      st_e=""
      for state_element in state:
        print(f"={state_element}")
        if sorted(name) == sorted(state_element):
          print(f"={name}")
          for n in range(len(name)):
            print(f"={n}")
            for se in range(len(state_element)):
              print(f"={se}")
              if state_element.strip()[se]==name.strip()[n]:
                print(f"={state_element.strip()[se]}")
                print("se={se}")
                st_e+=state[state_element].strip()[se]
      mb.update({name:st_e})
      print(f"mb={mb}")
    mbc=mb
    if self.mosf[f]!=c:
      mb[f"{f}{s}{c}"]=mbc[f"{f}{s}{self.mosf[c]}"]
      mb[f"{s}{c}"]=mbc[f"{f}{s}"]
      mb[f"{self.mosf[f]}{s}{c}"]=mbc[f"{f}{s}{c}"]
      mb[f"{self.mosf[f]}{s}"]=mbc[f"{s}{c}"]
      mb[f"{self.mosf[f]}{s}{self.mosf[c]}"]=mbc[f"{self.mosf[f]}{s}{c}"]
      mb[f"{s}{self.mosf[c]}"]=mbc[f"{self.mosf[f]}{s}"]
      mb[f"{f}{s}{self.mosf[c]}"]=mbc[f"{self.mosf[f]}{s}{self.mosf[c]}"]
      mb[f"{f}{s}"]=mbc[f"{s}{self.mosf[c]}"]
    elif self.mosf[f]==c:
      # moving_block={f s c,f s mosf[c],mosf[f] s c, mosf[f] s mosf[c],f s, s c , mosf[f] s, s mosf[c]}
      mb[f"{self.mosf[f]}{s}{c}"]=mbc[f"{f}{s}{self.mosf[c]}"]
      mb[f"{self.mosf[f]}{s}"]=mbc[f"{f}{s}"]
      mb[f"{self.mosf[f]}{s}{self.mosf[c]}"]=mbc[f"{f}{s}{c}"]
      mb[f"{s}{self.mosf[c]}"]=mbc[f"{s}{c}"]
      mb[f"{[f]}{s}{self.mosf[c]}"]=mbc[f"{self.mosf[f]}{s}{c}"]
      mb[f"{f}{s}"]=mbc[f"{self.mosf[f]}{s}"]
      mb[f"{f}{s}{c}"]=mbc[f"{self.mosf[f]}{s}{self.mosf[c]}"]
      mb[f"{s}{c}"]=mbc[f"{s}{self.mosf[c]}"]
    for state_element in state:
      st_e=""
      for name in moving_block:
        if sorted(name) == sorted(state_element):
               for se in range(len(state_element)):
                 for n in range(len(name)):
                   if state_element.strip()[se]==name.strip()[n]:
                     # state[state_element].append(mb[name].strip()[n])
                     st_e+=mb[name].strip()[n]
      state.update({state_element:st_e})
      print(f"state={state}")
    return state
  # def solver():
      # batch=27
      # block=20
      # epoches=20
      # for epoch in range(epoches):
        
  def moves(self, state, move_list=move_paths, move_history=""):
    moves_to=list(move_list)
    cur_state=state
    i=0
    states = {}
    puzzle_solve= False
    last_move=""
    move_path_history=list(move_history)
    while cur_state!=self.solution and i<len(moves_to):
      states[i] = self.mover(moves_to[i],cur_state)
      move_path_history.append(moves_to[i])
      # Prepare the JSONL entry
      data_entry = {
        "given state":"",
        "current state":states[i],
        "move": moves_to[i],
        "moved_steps_list":move_path_history,
        "metadata": {
          "source": "Fuzzle Solver",
          "length": len(move_path_history)
        }
        }
      # Append to the JSONL file
      with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data_entry) + '\n')
      print(f"Successfully Saved")
      last_move=moves_to[i]
      next_moves_list=[]
      # next_moves_list=next_moves(last_move)
      for to_move in moves_to:
        # if last_move != to_move:
        # if(last_move.strip()[:2]!=to_move.strip()[:2]):
        if last_move.strip()[:2]!=to_move.strip()[:2]:
          next_moves_list.append(to_move)
        # states[i], move_path_history, puzzle_solve = self.moves(states[i], next_moves_list, move_path_history)
      if states[i]==self.solution:
        puzzle_solve=True
        return states[i], move_path_history, puzzle_solve
      return self.moves(states[i], next_moves_list, move_path_history) ##
      i=i+1
if __name__=="__main__":
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
  cs=CubeSolver()
  result=cs.moves(state_given)
  print(result)

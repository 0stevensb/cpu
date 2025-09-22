memory = ["LOAD 1",
          "STORE 2",20
          "INPUT",
          "STORE 3",
          "INPUT",
          "STORE 0",
          "INPUT" ,
          "STORE 1",
          "ADDM 0",
          "STORE 0",
          "MLOAD 2",
          "ADD 1",
          "STORE 2",
          "IFJUMP 2 3 6",
          "OUTPUT 0",
          "HALT"] # Instructions in memory
accumulator = 0 # Register for calculations
program_counter = 0 # Tracks which instruction to fetch
ram = [0] * 16 # Simple RAM with 16 addresses
while True:
# FETCH
 instruction = memory[program_counter]
 program_counter += 1
# DECODE
 parts = instruction.split()
 opcode = parts[0]
# EXECUTE
 if opcode == "LOAD":
  accumulator = int(parts[1])
 elif opcode =="MLOAD":
  accumulator = ram[int(parts[1])]
 elif opcode == "ADD":
  accumulator += int(parts[1])
 elif opcode == "STORE":
  ram[int(parts[1])] = accumulator
 elif opcode == "SUB":
  accumulator -= int(parts[1])
 elif opcode == "INPUT":
  accumulator = int(input())
 elif opcode == "ADDM":
  accumulator+=ram[int(parts[1])]
 elif opcode == "SUBM":
  accumulator-=ram[int(parts[1])]
 elif opcode == "OUTPUT":
  print(ram[int(parts[1])])
 elif opcode == "JUMP":
  program_counter=int(parts[1])
 elif opcode == "IFJUMP":
  if ram[int(parts[1])] <ram[int(parts[2])]:
   program_counter= int(parts[3])
 elif opcode == "HALT":
  break
#print("RAM contents:", ram)
#
#print("Accumulator:", accumulator)
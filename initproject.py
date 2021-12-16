shopping = ["chleb","jajka"]
sklep = "Mięsnego"
for item in shopping:
  print(f"Idę do sklepu {sklep} i kupuję tam: {item}")
def get_no_of_elements(list):
    count = 0
    for element in shopping:
        count += 1
    return count

print("W sumie kupuję ", get_no_of_elements(shopping),"produktów")
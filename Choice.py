
def show_food(df):
    letter = input('Type the starting letters of the food you are looking for: \n')
    out = df[df['name'].str.startswith(letter)]     #tutti i cibi che iniziano con la lettera specificata dall'utente (letter)
    out = out.reset_index(drop=True)                  #reset degli indici delle righe, numerati  1, 2, ..., n
    print(out['name'])                              #return solamente della colonna name
    return

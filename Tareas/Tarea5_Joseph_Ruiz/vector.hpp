
//Librerías
#include<iostream>
#include <sstream>
//Espacio de nombres
using std::cout;
using std::endl;


namespace myvec{

  class Vector{
  
    public:
      
//Creación del constructor. Parámetros: número entero, componentes/entradas.
      Vector (int Size){
      
        cout << "Objeto Vector se ha creado"<< endl;
        Dimension = Size;        

        //Vector de Dimension Size y cero en todas las entradas por defecto
        V = new int [Dimension] {0};

        }
                
              
//-----Función de print: imprime el objeto vector
      
       void PrintVec(void){ 
       
         cout << "[ " ;         
         for(int i = 0; i < Dimension; i++) {
           cout<< *(V+i) <<" ";
         }
         cout << "]" << endl;
         
       }
       
//-----Función de inicialización de valores
       void SetPos(int entrada, int value){ 
         
         if (entrada > Dimension - 1)
            cout<< "ERROR: La posición excede el rango"<< endl;
         else
           *(V+entrada) = value;
       }
   
      
//-----Función de obtención de entrada
       int GetPos(int entrada){ 
         
         if (entrada > Dimension - 1){
           cout<< "ERROR: La posición excede el rango"<< endl;
           return 0;
         }
         else
            return *(V+entrada);
       }
   
   
//-----Función Dimension----> Size
       int GetSize(void){ 
         return Dimension; 
       }
       
//-----Sobrecarga del operador =
       void operator = (Vector V_1){

         if (V_1.GetSize() != Dimension){
           cout<< "ERROR: dimension de los objetos no coincide" << endl;
           
         }
         else {
           for(int i = 0; i < Dimension; i++)  
             *(V + i) = V_1.GetPos(i);           
         }
         
         
       }   


//-----Sobrecarga del operador +
       Vector operator + (Vector V_1){

         if (V_1.GetSize() != Dimension){
          cout<< "ERROR: dimension de los objetos no coincide" << endl;

           
         }
         else {
           Vector VSum(Dimension);
           for(int i = 0; i < Dimension; i++)  
             VSum.SetPos(i, V_1.GetPos(i) + *(V+i));
           return VSum;

         }
       } 

   
   
//-----Sobrecarga del operador -
       Vector operator - (Vector V_1){

         if (V_1.GetSize() != Dimension){
          cout<< "Los vectores son de tamaños diferentes. No se puede realizar la operación requerida." << endl;

           
         }
         else {
           Vector VSum(Dimension);
           for(int i = 0; i < Dimension; i++)  
             VSum.SetPos(i, V_1.GetPos(i) - *(V+i));
           return VSum;

         }
       } 
       
       
      
//-----Sobrecarga del operador []
       int& operator [] (int i){
         if (i < Dimension){
           return *(V+i);
         }
         else{
           cout << "Índice fuera del rango." << endl;
         }
       }
  
   
//Atributo privado
    private:
      int Dimension;
      int *V;
  
  };
}

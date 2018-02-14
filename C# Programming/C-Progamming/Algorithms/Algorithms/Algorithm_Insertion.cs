using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithms
{
    class Algorithm_Insertion
    {
        // assign space for 10 integer values
        private int[] values = new int[10];

        //public constructor (note no return type)
        public Algorithm_Insertion()
        {
            // instance of the Random class.
            Random random = new Random();

            for (int i = 0; i < 10; i++)
            {
                // assign a random value between 0 and 250 to each entry in the values array.
                values[i] = random.Next(250);
            }

            PrintValues();
        }

        public void PrintValues()
        {
            for (int i = 0; i < values.Length; i++)
            {
                // "ToString" allows us to combine the integer value with the space without C# complaining.
                Console.Write(values[i].ToString() + " ");
            }
            Console.WriteLine();
        }

        // class for Insertion sort implementation.
        public void SortValues()
        {

            int length = values.Length;

            for (int i = 1; i < length; i++)
            {
                int j = i;

                while ((j > 0) && (values[j] < values[j - 1]))
                {
                    // swaps j with previous value until j is larger than j-1 starting at values[1]
                    int k = j - 1;
                    int temp = values[k];
                    values[k] = values[j];
                    values[j] = temp;

                    j--;
                }
                PrintValues();
            }
        }
    }
 }

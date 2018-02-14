using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            Algorithm_Insertion insertion = new Algorithm_Insertion();
            insertion.SortValues();
            Algorithm_Selection selection = new Algorithm_Selection();
            selection.SortValues();
        }
    }
}

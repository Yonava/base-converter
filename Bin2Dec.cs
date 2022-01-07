using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS114_First_Lab
{
    internal class Program
    {
        static double BinaryToDecimal(string num)
        {
            double output = 0;
            int index = 0;

            char[] charArray = num.ToCharArray();
            Array.Reverse(charArray);
            num = new string(charArray);

            foreach (char c in num)
            {
                if ((int)c == 49)
                {
                    output += Math.Pow(2, index);
                }
                index++;
            }
            return output;
        }
        static void Main(string[] args)
        {
            string input;

            Console.Write("Enter Binary Number: ");
            input = Console.ReadLine();

            if (String.IsNullOrEmpty(input))
            {
                Console.WriteLine("Binary Numbers Only!");
                return;
            }

            bool valid = true;
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] != '0' && input[i] != '1')
                {
                    valid = false;
                    break;
                }
            }
            if (!valid)
            {
                Console.WriteLine(input + " Isn't Valid Binary!");
            } 
            else
            {
                double num = BinaryToDecimal(input);
                Console.WriteLine(input + " == " + num + " in Decimal Form");
            }

            Console.ReadLine();
        }
    }
}

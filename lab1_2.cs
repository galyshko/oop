using System;
using System.Collections.Generic;

public class GeometricProgression
{
    // Статична змінна для збереження екземплярів класу
    public static List<GeometricProgression> Instances = new List<GeometricProgression>();

    // Параметри прогресії
    private double a;
    private double b;

    // Ініціалізація геометричної прогресії з першим елементом a і знаменником b
    public GeometricProgression(double a, double b)
    {
        if (b == 0)
        {
            throw new ArgumentException("Знаменник прогресії не може бути нульовим.");
        }

        this.a = a;
        this.b = b;

        Instances.Add(this);
    }

    // Обчислює n-й елемент геометричної прогресії
    public double NthElement(int n)
    {
        return a * Math.Pow(b, n - 1);
    }

    // Генерує список елементів прогресії від k-го до m-го включно
    public List<double> Sequence(int k, int m)
    {
        List<double> sequence = new List<double>();
        for (int i = k; i <= m; i++)
        {
            sequence.Add(NthElement(i));
        }
        return sequence;
    }

    // Оновлює параметри прогресії (перший елемент і знаменник)
    public void UpdateParams(double a, double b)
    {
        if (b == 0)
        {
            throw new ArgumentException("Знаменник прогресії не може бути нульовим.");
        }

        this.a = a;
        this.b = b;
    }

    // Перевіряє рівність двох прогресій за першими елементами і знаменником
    public override bool Equals(object obj)
    {
        if (obj is GeometricProgression other)
        {
            return this.a == other.a && this.b == other.b;
        }
        return false;
    }



    // Повертає рядкове представлення перших семи елементів прогресії
    public override string ToString()
    {
        var firstSeven = string.Join(", ", Sequence(1, 7));
        return $"& {a}, {b}: {firstSeven}";
    }

    // Виводить інформацію про всі існуючі екземпляри прогресій
    public static void ShowInstances()
    {
        foreach (var instance in Instances)
        {
            Console.WriteLine(instance);
        }
    }
}

// Тестування класу
public class Program
{
    public static void Main()
    {
        // Створення екземплярів
        GeometricProgression gp1 = new GeometricProgression(1, 2);
        GeometricProgression gp2 = new GeometricProgression(2, 2);
        GeometricProgression gp3 = new GeometricProgression(2, 0.5);

        // Виведення інформації
        Console.WriteLine(gp1);
        Console.WriteLine(gp2);
        Console.WriteLine(gp3);

        // Отримання 5-го елемента
        Console.WriteLine("\n5-й елемент gp1: " + gp1.NthElement(5));

        // Послідовність від 3-го до 6-го елемента
        Console.WriteLine("\nЕлементи з 3 по 6 gp2: " + string.Join(", ", gp2.Sequence(3, 6)));

        // Зміна параметрів
        gp1.UpdateParams(3, 2);
        Console.WriteLine("\ngp1 Після зміни параметрів: " + gp1);

        // Перевірка рівності
        Console.WriteLine("\nЧи рівні gp1 і gp3? " + (gp1.Equals(gp3) ? "Так" : "Ні"));

        // Виведення всіх екземплярів
        GeometricProgression.ShowInstances();
    }
}

 using System;

    namespace factoryPattern
    {
        public interface IButton
        {
            string click();
        }

        class WebButton : IButton
        {
            public string click()
            {
                return "{returns a new web button click}";
            }
        }

        class MobileButton : IButton
        {
            public string click()
            {
                return "{returns a new mobile button click}";
            }
        }

        public abstract class Dialog
        {
            public abstract IButton FactoryMethod();
            public string SomeOperation()
            {
                var button = FactoryMethod();
                return "creators code working with " + button.click();
            }
        }

        public class WebDialog : Dialog
        {
            public override IButton FactoryMethod()
            {
                return new WebButton();
            }

        }
        public class MobileDialog : Dialog
        {
            public override IButton FactoryMethod()
            {
                return new MobileButton();
            }

        }

        class ClientClass
        {
            public void Main()

            {
                ClientCall(new WebDialog());
                ClientCall(new MobileDialog());
            }

            public void ClientCall(Dialog dialog)
            {
                Console.WriteLine("Client: I'm not aware of the creator's class," +
                    "but it still works.\n" + dialog.SomeOperation());
                // ...
            }


            class MainClass
            {
                static void Main(string[] args)
                {
                    new ClientClass().Main();
                }
            }
        }
using Neo.Core;
using Neo.Properties;
using Neo.SmartContract;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Windows.Forms;

namespace Neo.UI
{
    internal static class Helper
    {
        private static Dictionary<Type, Form> tool_forms = new Dictionary<Type, Form>();

        private static void Helper_FormClosing(object sender, FormClosingEventArgs e)
        {
            tool_forms.Remove(sender.GetType());
        }

        public static void Show<T>() where T : Form, new()
        {
            Type t = typeof(T);
            if (!tool_forms.ContainsKey(t))
            {
                tool_forms.Add(t, new T());
                tool_forms[t].FormClosing += Helper_FormClosing;
            }
            tool_forms[t].Show();
            tool_forms[t].Activate();
        }

        public static void SignAndShowInformation(Transaction tx)
        {
            if (tx == null)
            {
                MessageBox.Show(Strings.InsufficientFunds);
                return;
            }
            ContractParametersContext context;
            try
            {
                context = new ContractParametersContext(tx);
            }
            catch (InvalidOperationException)
            {
                MessageBox.Show(Strings.UnsynchronizedBlock);
                return;
            }
            Program.CurrentWallet.Sign(context);
            if (context.Completed)
            {
                context.Verifiable.Scripts = context.GetScripts();
                Program.CurrentWallet.SaveTransaction(tx);
                Program.LocalNode.Relay(tx);
                WriteTxToFile(tx);
                InformationBox.Show(tx.Hash.ToString(), Strings.SendTxSucceedMessage, Strings.SendTxSucceedTitle);
            }
            else
            {
                InformationBox.Show(context.ToString(), Strings.IncompletedSignatureMessage, Strings.IncompletedSignatureTitle);
            }
        }

        public static void WriteTxToFile(Transaction tx)
        {
            string filePath = "C:\\";
            StreamWriter sw = null;
            try
            {
                sw = new StreamWriter(filePath + "NeoLogs.txt", true);
                sw.WriteLine("Node: " + GetLocalIPAddress() +
                             " Time: " + DateTime.Now.ToString() +
                             " Tx: " + tx.Hash.ToString());
                sw.Flush();
                sw.Close();
            }
            catch
            {
                Console.WriteLine("Exception writing tx to file");
            }
        }

        public static string GetLocalIPAddress()
        {
            var host = Dns.GetHostEntry(Dns.GetHostName());
            foreach (var ip in host.AddressList)
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    return ip.ToString();
                }
            }
            throw new Exception("Local IP Address Not Found!");
        }

        public static String DisplayLocalHostName()
        {
            try
            {
                // Get the local computer host name.
                String hostName = Dns.GetHostName();
                return hostName;
            }
            catch (SocketException e)
            {
                Console.WriteLine("SocketException caught!!!");
                Console.WriteLine("Source : " + e.Source);
                Console.WriteLine("Message : " + e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception caught!!!");
                Console.WriteLine("Source : " + e.Source);
                Console.WriteLine("Message : " + e.Message);
            }
            return "Null";
        }
    }
}

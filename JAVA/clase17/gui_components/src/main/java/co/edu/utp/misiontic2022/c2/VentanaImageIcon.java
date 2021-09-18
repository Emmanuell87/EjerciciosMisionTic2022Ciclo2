package co.edu.utp.misiontic2022.c2;

import java.awt.*;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class VentanaImageIcon extends JFrame{
    
    public VentanaImageIcon(String ruta){
        Container c = getContentPane();
        c.setLayout(new FlowLayout());
        //
        ImageIcon icono = new ImageIcon(ruta);
        JButton boton = new JButton(icono);
        c.add(new JLabel("", icono, JLabel.CENTER));

        c.add(boton);

        //
        setSize(600, 600);
        setVisible(true);
    }

    public static void main(String[] args) {
        new VentanaImageIcon("C:/Users/emmanuel/Desktop/IMASTER_CURSO/JAVA/clase17/gui_components/ImagePanda.jpg");
        
    }

}

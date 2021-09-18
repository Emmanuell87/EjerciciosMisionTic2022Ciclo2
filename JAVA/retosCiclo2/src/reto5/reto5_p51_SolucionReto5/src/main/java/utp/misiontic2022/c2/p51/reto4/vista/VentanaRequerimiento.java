package utp.misiontic2022.c2.p51.reto4.vista;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.JTable;
import javax.swing.table.AbstractTableModel;
import java.awt.BorderLayout;
import java.sql.SQLException;
import java.util.ArrayList;

import utp.misiontic2022.c2.p51.reto4.controlador.ControladorRequerimientos;
import utp.misiontic2022.c2.p51.reto4.modelo.vo.Requerimiento_1;
import utp.misiontic2022.c2.p51.reto4.modelo.vo.Requerimiento_2;
import utp.misiontic2022.c2.p51.reto4.modelo.vo.Requerimiento_3;

public class VentanaRequerimiento extends JFrame {

    private ControladorRequerimientos controlador;
    private JTable tablaConsulta1;
    private JTable tablaConsulta2;
    private JTable tablaConsulta3;



    public VentanaRequerimiento(){
        controlador = new ControladorRequerimientos();
        
        initUI();
        setLocationRelativeTo(null);
    }

    private void initUI(){
        setTitle("Interfaz Reto 5");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(800, 600);

        var tbd = new JTabbedPane();

        getContentPane().add(tbd, BorderLayout.CENTER);

        var panel_1 = new JPanel();

        panel_1.setLayout(new BorderLayout());
        tbd.addTab("Consulta Requerimiento", panel_1);

        var panelConsulta1 = new JPanel();
        panelConsulta1.add(new JLabel("Requerimiento 1"));
        var btnConsulta1 = new JButton("Consultar!");
        btnConsulta1.addActionListener(e -> cargarTablaConsulta1());
        panelConsulta1.add(btnConsulta1);

        panel_1.add(panelConsulta1, BorderLayout.PAGE_START);

        tablaConsulta1 = new JTable();
        panel_1.add(new JScrollPane(tablaConsulta1), BorderLayout.CENTER);


        
        var panel_2 = new JPanel();

        panel_2.setLayout(new BorderLayout());
        tbd.addTab("Consulta Requerimiento", panel_2);

        var panelConsulta2 = new JPanel();
        panelConsulta2.add(new JLabel("Requerimiento 2"));
        var btnConsulta2 = new JButton("Consultar!");
        btnConsulta2.addActionListener(e -> cargarTablaConsulta2());
        panelConsulta2.add(btnConsulta2);

        panel_2.add(panelConsulta2, BorderLayout.PAGE_START);
        tablaConsulta2 = new JTable();
        panel_2.add(new JScrollPane(tablaConsulta2), BorderLayout.CENTER);



        var panel_3 = new JPanel();

        panel_3.setLayout(new BorderLayout());
        tbd.addTab("Consulta Requerimiento", panel_3);

        var panelConsulta3 = new JPanel();
        panelConsulta3.add(new JLabel("Requerimiento 3"));
        var btnConsulta3 = new JButton("Consultar!");
        btnConsulta3.addActionListener(e -> cargarTablaConsulta3());
        panelConsulta3.add(btnConsulta3);

        panel_3.add(panelConsulta3, BorderLayout.PAGE_START);
        tablaConsulta3 = new JTable();
        panel_3.add(new JScrollPane(tablaConsulta3), BorderLayout.CENTER);





    }


    // Metodos para cargar las tablas de las consultas respectivamentes 
    private void cargarTablaConsulta1() {
        try {
            var lista = controlador.consultarRequerimiento1();
            var tableModel = new Requerimiento1TableModel();
            tableModel.setData(lista);

            tablaConsulta1.setModel(tableModel);

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), getTitle(), JOptionPane.ERROR_MESSAGE);
        }
    }

    private void cargarTablaConsulta2() {
        try {
            var lista = controlador.consultarRequerimiento2();
            var tableModel = new Requerimiento2TableModel();
            tableModel.setData(lista);

            tablaConsulta2.setModel(tableModel);

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), getTitle(), JOptionPane.ERROR_MESSAGE);
        }
    }

    private void cargarTablaConsulta3() {
        try {
            var lista = controlador.consultarRequerimiento3();
            var tableModel = new Requerimiento3TableModel();
            tableModel.setData(lista);

            tablaConsulta3.setModel(tableModel);

        } catch (SQLException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), getTitle(), JOptionPane.ERROR_MESSAGE);
        }
    }


    // metodos conectar conectarse con las consultas y obtener sus datos
    private class Requerimiento1TableModel extends AbstractTableModel {

        private ArrayList<Requerimiento_1> data;

        public void setData(ArrayList<Requerimiento_1> data){
            this.data = data;
        }

        @Override
        public String getColumnName(int column){
            switch(column) {
                case 0:
                    return "Nombre Material";
                case 1:
                    return "Precio Unidad";
            }
            return super.getColumnName(column);
        }

        @Override
        public int getRowCount() {
            return data.size();
        }

        @Override
        public int getColumnCount() {
            return 2;
        }

        @Override
        public Object getValueAt(int rowIndex, int columnIndex) {
            var registro = data.get(rowIndex);

            switch(columnIndex) {
                case 0:
                    return registro.getNombreMaterial();
                case 1:
                    return registro.getPrecioUnidad();
            }

            return null;
        }
        
    }


    private class Requerimiento2TableModel extends AbstractTableModel {

        private ArrayList<Requerimiento_2> data;

        public void setData(ArrayList<Requerimiento_2> data){
            this.data = data;
        }

        @Override
        public String getColumnName(int column){
            switch(column) {
                case 0:
                    return "Constructora";
                case 1:
                    return "Ciudad";
            }
            return super.getColumnName(column);
        }

        @Override
        public int getRowCount() {
            return data.size();
        }

        @Override
        public int getColumnCount() {
            return 2;
        }

        @Override
        public Object getValueAt(int rowIndex, int columnIndex) {
            var registro = data.get(rowIndex);

            switch(columnIndex) {
                case 0:
                    return registro.getConstructora();
                case 1:
                    return registro.getCiudad();
            }

            return null;
        }  
   
    }

    private class Requerimiento3TableModel extends AbstractTableModel {
    
        private ArrayList<Requerimiento_3> data;

        public void setData(ArrayList<Requerimiento_3> data){
            this.data = data;
        }

        @Override
        public String getColumnName(int column){
            switch(column) {
                case 0:
                    return "Proveedor";
                case 1:
                    return "Nombre Material";
                case 2:
                    return "IMportado";
                case 3:
                    return "Precio Unidad";
                case 4:
                    return "Cantidad";
            }
            return super.getColumnName(column);
        }

        @Override
        public int getRowCount() {
            return data.size();
        }

        @Override
        public int getColumnCount() {
            return 5;
        }

        @Override
        public Object getValueAt(int rowIndex, int columnIndex) {
            var registro = data.get(rowIndex);

            switch(columnIndex) {
                case 0:
                    return registro.getProveedor();
                case 1:
                    return registro.getNombreMaterial();
                case 2:
                    return registro.getImportado();
                case 3:
                    return registro.getPrecioUnidad();
                case 4:
                    return registro.getCantidad();
                
            }

            return null;
        }
    }

    
}

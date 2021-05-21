import javax.swing.*;

public class costCalculate {
    public static void main (String args[]) {
        cylinderType PaintCan = new cylinderType();
        PaintCan.setRadius();
        PaintCan.setHeight();
        PaintCan.setShipCostPerLiter();
        PaintCan.setPaintCostPerSqF();

        float ShipCost;
        float PaintCost;

        ShipCost = (float) (PaintCan.getShipCostPerLiter() * PaintCan.getHeight() * PaintCan.getRadius() * PaintCan.getRadius() * 3.14159 * 28.317);
        PaintCost = (float) (PaintCan.getPaintCostPerSqF() * PaintCan.getRadius() * PaintCan.getHeight() * 2 * 3.14159);

        JOptionPane.showMessageDialog(null, "Shipping cost is: " + ShipCost);
        JOptionPane.showMessageDialog(null, "Paint cost is: " + PaintCost);
    }
}

import javax.swing.*;

public class cylinderType {
    private int Radius;
    private int Height;
    private float ShipCostPerLiter;
    private float PaintCostPerSqF;

    public void setRadius() {
        this.Radius = Integer.parseInt(JOptionPane.showInputDialog("Enter cylinder radius in feet: "));
    }

    public void setHeight() {
        this.Height = Integer.parseInt(JOptionPane.showInputDialog("Enter cylinder height in feet: "));
    }

    public void setShipCostPerLiter() {
        this.ShipCostPerLiter = Integer.parseInt(JOptionPane.showInputDialog("Enter shipping cost per liter: "));
    }

    public void setPaintCostPerSqF() {
        this.PaintCostPerSqF = Integer.parseInt(JOptionPane.showInputDialog("Enter paint cost per square foot: "));
    }

    public int getRadius() { return Radius; }

    public int getHeight() { return Height; }

    public float getShipCostPerLiter() {return ShipCostPerLiter; }

    public float getPaintCostPerSqF() {return PaintCostPerSqF; }
}

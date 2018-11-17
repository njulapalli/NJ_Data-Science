
Sub alphab()
Dim ticker As String
Dim TotalStockVolume As Double

Dim Summary_Table_Row As Integer
Summary_Table_Row = 2

Dim RowsInSheet As Long
RowsInSheet = Cells(Rows.Count, "A").End(xlUp).Row

TotalStockVolume = 0
Range("I" & 1) = "Ticker"
Range("J" & 1) = "Total Stock Volume"

For i = 2 To RowsInSheet
TotalStockVolume = TotalStockVolume + (Cells(i, 7).Value / 1000000)

If Cells(i + 1, 1).Value <> Cells(i, 1) Then
    ticker = Cells(i, 1).Value

    ' copy to summary table
    Range("I" & Summary_Table_Row).Value = ticker
    Range("J" & Summary_Table_Row).Value = (TotalStockVolume * 1000000)

    ' reset total volume to for next ticker volume calculation
    TotalStockVolume = 0
    Summary_Table_Row = Summary_Table_Row + 1

End If

Next i

End Sub

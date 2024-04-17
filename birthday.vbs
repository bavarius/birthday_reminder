On Error Resume Next
Dim objFileSystem, objFile
Dim szConfigFile, szBirthday, szName, szThisYear, szNextYear
Dim szComparisonDate, szMessage, szYearOfBirth
Dim iTime, iTemp, iDifference, iAge

' Initialisierungen
szConfigFile = "BIRTHDAY.INI"
iTime = 15 ' Wie viele Tage vor dem Geburtstag wird gemeldet?
szMessage = ""
szThisYear = CStr(Year(Date))
szNextYear = CStr(Year(Date) + 1)

Set objFileSystem = CreateObject("Scripting.FileSystemObject")

' Config-Datei ermitteln, ...
If objFileSystem.FileExists(szConfigFile) Then
    ' ... öffnen...
    Set objFile = objFileSystem.OpenTextFile(szConfigFile)
    
    ' ... und zeilenweise abarbeiten
    Do Until objFile.atEndOfStream
    
       ' Geburtstag und Name des Geburtstagskindes lesen
       szBirthday = objFile.read(6) ' lese die ersten 6 Zeichen
       szName = objFile.readLine
       iTemp = InStr(szName, "(")
       
       If iTemp Then ' String enthält "("
          szYearOfBirth = Mid(szName, InStrRev(szName, ")") - 4, 4)
          szName = Trim(Left(szName, iTemp - 1))
       Else
          szYearOfBirth = ""
          szName = Trim(szName)
       End If
       
       ' Wieviele Tage sind es noch bis zum nächsten Geburtstag?
       szComparisonDate = szBirthday & szThisYear
       iDifference = DateDiff("y", Date, DateValue(szComparisonDate))
    
       ' Falls der nächste Geburtstag allerdings erst im nächsten Jahr liegt
       If iDifference < 0 Then
          szComparisonDate = szBirthday & szNextYear
          iDifference = DateDiff("y", Date, DateValue(szComparisonDate))
          If szYearOfBirth <> "" Then
             iAge = CInt(szNextYear) - CInt(szYearOfBirth)
          End If
       Else
          If szYearOfBirth <> "" Then
             iAge = CInt(szThisYear) - CInt(szYearOfBirth)
          End If
       End If
       
       ' Wenn die Anzahl der Tage innerhalb der Frist liegt
       If iDifference <= iTime Then
          If szYearOfBirth = "" Then
             szMessage = szMessage & szName
          Else
             szMessage = szMessage & szName & " wird " & iAge
          End If
          
          ' schreibe "H E U T E" oder "M O R G E N", wenn angebracht
          If iDifference = 0 Then
              szMessage = szMessage & " am " & szComparisonDate & " - H E U T E !" & vbCrLf
          ElseIf iDifference = 1 Then
              szMessage = szMessage & " am " & szComparisonDate & " - M O R G E N !" & vbCrLf
          Else
              szMessage = szMessage & " am " & szComparisonDate & " - noch " & iDifference & " Tage" & vbCrLf
          End If
       End If
    Loop
    objFile.Close

Else
   MsgBox "Die Config-Datei " & szConfigFile & " ist nicht vorhanden!", vbCritical, "Fehler"
End If

' Falls vorhanden, Liste der nächsten Geburtstage ausgeben
If szMessage <> "" Then
   MsgBox szMessage, vbInformation, "Die nächsten Geburtstage"
End If